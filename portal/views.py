from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users import models
from .models import ReviewProfile, Job, ProgressReport, Application
from django.db.models import Q

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

from messenger.models import Conversation


class HomePageView(TemplateView):
    template_name = 'home.html'


class HelpPageView(TemplateView):
    template_name = 'help.html'


class ShowCompanies(ListView):
    template_name = 'companies.html'
    model = models.Employer
    context_object_name = 'all_companies'


class GenericJobView(DetailView):
    model = Job
    template_name = 'portal/generic_job.html'
    context_object_name = 'generic_job'

    def get_context_data(self, **kwargs):
        context = super(GenericJobView, self).get_context_data(**kwargs)
        stud = models.Student(user=self.request.user)
        job = self.object.pk

        application = Application.objects.filter(student_id=stud, job_id=job)

        if application.exists():
            context['applied'] = 'T'
        else:
            context['applied'] = 'F'

        context['student'] = stud
        return context


class ListEmployeesViewAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.Employer
    template_name = 'portal/list_employees.html'
    context_object_name = 'admin_list_employees_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class EmployerProfileViewGeneric(DetailView):
    model = models.Employer
    api_key = settings.GOOGLE_MAPS_API_KEY
    api_key_places = settings.POSITION_API
    template_name = 'portal/employer_profile.html'
    context_object_name = 'employer_profile_view_generic'

    def get_context_data(self, **kwargs):
        context = super(EmployerProfileViewGeneric, self).get_context_data(**kwargs)
        context['google_maps_api_key'] = self.api_key
        context['positions_api_key'] = self.api_key_places
        return context


class ShowContactPersonGeneric(DetailView):
    model = models.ContactPerson
    template_name = 'portal/show_contact_person.html'
    context_object_name = 'contact_person_view_generic'
    login_url = 'login'


class ShowHRDirectorGeneric(DetailView):
    model = models.HRDirector
    template_name = 'portal/show_hr_directore.html'
    context_object_name = 'hr_director_view_generic'
    login_url = 'login'


class UpdateEmployerProfileStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ReviewProfile
    template_name = 'portal/update_employer_status.html'
    fields = ('review_status', 'reason')
    context_object_name = 'update_employer_profile_view'
    login_url = 'login'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('admin_list_employers', kwargs={"pk": pk})

    def form_valid(self, form):
        admin = models.GIUAdmin(user=self.request.user)
        form.instance.admin_id = admin

        message = Mail(
            from_email='iyadelwy@gmail.com',
            to_emails=admin.user.email,
            subject='GIU Internship Portal',
            html_content='<h1>Yay!</h1>'
                         '<h3>Your profile has been acceoted.</h3>'
                         '<p>Feel free to post jobs, talk to students and if any complication should arise, '
                         'please do not hesitate to contact us.</p>'
        )
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_admin


class ListFacRepAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.FacultyRepresentative
    template_name = 'portal/list_fac_admin.html'
    context_object_name = 'admin_list_fac_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class ListStudentsAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.Student
    template_name = 'portal/list_students_admin.html'
    context_object_name = 'admin_list_students_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.User
    template_name = 'editusers/user_delete.html'
    context_object_name = 'user_delete_view'
    success_url = reverse_lazy('admin_profile')

    def test_func(self):
        return self.request.user.is_admin

    def get_success_url(self):
        return reverse('admin_profile', args=[self.request.user.pk])


class StudentProfileViewGeneric(DetailView):
    model = models.Student
    template_name = 'portal/student_profile.html'
    context_object_name = 'student_profile_view_generic'
    login_url = 'login'


class StudentPhoneViewGeneric(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.StudentPhoneNumbers
    template_name = 'portal/student_phone_numbers.html'
    context_object_name = 'student_phone_list_generic'
    login_url = 'login'

    def get_queryset(self):
        # std = models.Student(user=self.request.user)
        queryset = models.StudentPhoneNumbers.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    def test_func(self):
        return self.request.user.is_employer or \
               self.request.user.is_academic_advisor or self.request.user.is_career_office_coordinator or \
               self.request.user.is_faculty_representative or self.request.user.is_admin


class ListAcademicAdvisorAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.AcademicAdvisor
    template_name = 'portal/list_academic_advsior_admin.html'
    context_object_name = 'admin_list_academic_advisor_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class ListCareerOCAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.CareerOfficeCoordinator
    template_name = 'portal/list_career_oc_admin.html'
    context_object_name = 'admin_list_career_oc_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class ListAcademicAdvisorCOC(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.AcademicAdvisor
    template_name = 'portal/list_academic_advisors_by_coc.html'
    context_object_name = 'coc_list_academic_advisor_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_career_office_coordinator


class EmployerPostsJobView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Job
    fields = ('title', 'job_description', 'department', 'job_start_date', 'job_end_date', 'application_deadline',
              'num_of_available_internships', 'salary_range', 'qualifications', 'job_location', 'job_type',
              'allowed_faculties', 'required_semesters', 'application_link',
              'application_email')
    template_name = 'portal/employer_posts_job.html'
    context_object_name = 'employer_posts_job'
    login_url = 'login'
    success_url = reverse_lazy('employer_job_post_successful')

    def get_success_url(self):
        return reverse('employer_job_post_successful', args=[self.request.user.pk])

    def form_valid(self, form):
        employer = models.Employer(user=self.request.user)
        form.instance.employer_id = employer
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_employer


class EmployerJobPostSuccessful(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'portal/job_post_successful.html'
    model = models.Employer
    login_url = 'login'
    context_object_name = 'job_post_successful'

    def test_func(self):
        employer = models.Employer.objects.filter(user=self.request.user)[0]
        rev = ReviewProfile.objects.filter(employer_id=employer)[0]
        return rev.review_status == 'Accepted'


class EmployerStatusNotAccepted(LoginRequiredMixin, DetailView):
    template_name = 'portal/employer_status_not_accepted.html'
    model = models.Employer
    login_url = 'login'
    context_object_name = 'employer_status_not_accepted'


class ShowPostedJobsEmployerView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/employer_views_jobs.html'
    context_object_name = 'employer_views_jobs'
    login_url = 'login'

    def get_queryset(self):
        emp = models.Employer(user=self.request.user)
        return Job.objects.filter(employer_id=emp)

    def test_func(self):
        return self.request.user.is_employer


class ShowJobForEmployer(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = 'portal/employer_views_own_job.html'
    context_object_name = 'employer_views_own_jobs'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer


class EmployerUpdateJob(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ('title', 'job_description', 'department', 'job_start_date', 'job_end_date', 'application_deadline',
              'num_of_available_internships', 'salary_range', 'qualifications', 'job_location', 'job_type',
              'allowed_faculties', 'required_semesters', 'application_link',
              'application_email')
    template_name = 'portal/employer_updates_job.html'
    context_object_name = 'employer_edits_job'
    login_url = 'login'
    success_url = 'employer_show_job'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('employer_show_job', kwargs={"pk": pk})

    def test_func(self):
        return self.request.user.is_employer


class EmployerUpdateJobVisibility(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ('post_is_up',)
    template_name = 'portal/employer_updates_job_visibility.html'
    context_object_name = 'employer_edits_job'
    login_url = 'login'
    success_url = 'employer_show_job'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('employer_show_job', kwargs={"pk": pk})

    def test_func(self):
        return self.request.user.is_employer


class ShowAllApplicationsByCompany(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_views_all_applications_by_company.html'
    context_object_name = 'employer_views_all_applications_by_company'
    login_url = 'login'
    queryset = Application.objects.order_by('application_date')

    def get_context_data(self, **kwargs):
        context = super(ShowAllApplicationsByCompany, self).get_context_data(**kwargs)
        # context['company_name'] = self.object_list[0].job_id.employer_id.company_name

        convo = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        if convo.exists():
            context['exists'] = True
        else:
            context['exists'] = False

        return context

    def test_func(self):
        return self.request.user.is_employer


# class ShowAllApplicationsByJob(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Application
#     template_name = 'portal/employer_views_all_applications_by_job.html'
#     context_object_name = 'employer_views_all_applications_by_job'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_employer


class EmployerChangesStudentApplicationStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    fields = ('application_status',)
    template_name = 'portal/employer_changes_application_status.html'
    context_object_name = 'employer_changes_application_status'
    login_url = 'login'
    success_url = reverse_lazy('employer_profile')

    def form_valid(self, form):
        status = form.cleaned_data['application_status']
        if status == 'Accepted':
            form.instance.has_started = True
            std = self.object.student_id
            form.instance.student_id = std
            models.Student.objects.filter(user=std.user).update(current_aa=self.object.job_id.aa_id)
            models.Student.objects.filter(user=std.user).update(is_in_job=True)
            # Job.objects.filter(job_id=self.object.job_id.job_id).active_student = std
            ProgressReport.objects.create(student_id=self.object.student_id,
                                          application_id=self.object,
                                          academic_advisor_id=self.object.job_id.aa_id,
                                          progress_report_title='Initial Report',
                                          progress_report_description='This is your first progress report. It '
                                                                      'is meant to serve as a key to indicate '
                                                                      'the acceptance of your internship/').save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('employer_profile', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_employer


class EmployerShowAllActiveInternships(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_view_all_active_internships.html'
    context_object_name = 'employer_view_active_internships'
    login_url = 'login'

    # def get_queryset(self):
    #     return self.object_list.filter(job)

    def test_func(self):
        return self.request.user.is_employer


# put option to pay
class EmployerEndInternship(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    template_name = 'portal/employer_end_active_internship.html'
    context_object_name = 'employer_end_active_internship'
    login_url = 'login'
    fields = ('has_ended',)
    success_url = 'employer_profile'

    def get_success_url(self):
        return reverse('employer_profile', args=[self.request.user.pk])

    def form_valid(self, form):
        form.instance.has_started = False
        std = self.object.student_id
        models.Student.objects.filter(user=std.user).update(current_aa=None)
        models.Student.objects.filter(user=std.user).update(is_in_job=False)

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_employer


class EmployerPayStudentForInternship(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_pay_for_internship.html'
    context_object_name = 'employer_pay_for_internship'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(EmployerPayStudentForInternship, self).get_context_data(**kwargs)
        # context['company_name'] = self.object_list[0].job_id.employer_id.company_name

        convo = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        if convo.exists():
            context['exists'] = True
        else:
            context['exists'] = False

        return context

    def test_func(self):
        return self.request.user.is_employer


class PaymentView(TemplateView):
    template_name = 'portal/payment.html'
    context_object_name = 'employer_pay'


class ViewJobsGeneric(ListView):
    model = Job
    template_name = 'portal/view_jobs_generic.html'
    context_object_name = 'generic_job_view'


class AdminShowJobs(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/admin_views_all_jobs.html'
    context_object_name = 'admin_views_all_jobs'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdminShowJobs, self).get_context_data(**kwargs)
        adm = models.GIUAdmin(user=self.request.user)
        context['admin_pk'] = adm
        return context

    def test_func(self):
        return self.request.user.is_admin


# class ShowJobForAdmin(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Job
#     template_name = 'portal/admin_views_job.html'
#     context_object_name = 'admin_views_job'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_admin


class AdminChangeJobStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = 'portal/admin_change_job_status.html'
    fields = ('visibility_admin',)

    context_object_name = 'admin_change_job_status'
    login_url = 'login'
    success_url = reverse_lazy('admin_views_jobs')

    def get_success_url(self):
        return reverse('admin_views_jobs', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_admin


class FacRepShowJobs(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/fac_rep_show_jobs.html'
    context_object_name = 'fac_rep_show_jobs'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FacRepShowJobs, self).get_context_data(**kwargs)
        d = models.FacultyRepresentative.objects.all().filter(user=self.request.user)
        context['faculty_rep'] = d[0].faculty
        return context

    def test_func(self):
        return self.request.user.is_faculty_representative


# class ShowJobForFacRep(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Job
#     template_name = 'portal/fac_rep_views_job.html'
#     context_object_name = 'fac_rep_views_job'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_faculty_representative


class FacRepChangeJobStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = 'portal/fac_rep_changes_job_status.html'
    fields = ('visibility_fac_rep',)
    context_object_name = 'fac_rep_changes_job_status'
    login_url = 'login'
    success_url = reverse_lazy('fac_rep_views_jobs')

    def get_success_url(self):
        return reverse('fac_rep_views_jobs', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_faculty_representative


class CocShowApplications(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/coc_views_application.html'
    context_object_name = 'coc_views_application'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(CocShowApplications, self).get_context_data(**kwargs)
        # context['company_name'] = self.object_list[0].job_id.employer_id.company_name

        convo = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        if convo.exists():
            context['exists'] = True
        else:
            context['exists'] = False

        return context

    def test_func(self):
        return self.request.user.is_career_office_coordinator


class CocUpdateStudentApplicationStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    fields = ('visibility_for_employer',)
    template_name = 'portal/coc_changes_application_status.html'
    context_object_name = 'coc_changes_application_status'
    login_url = 'login'
    success_url = reverse_lazy('coc_show_applications')

    def get_success_url(self):
        return reverse('coc_show_applications', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_career_office_coordinator


# here also assign aadvisor when accepting

class CocAssignsAcademicAdviserToJob(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ('aa_id',)
    login_url = 'login'
    template_name = 'portal/coc_assigns_aa_to_job.html'
    success_url = reverse_lazy('coc_show_applications')

    def get_success_url(self):
        return reverse('coc_show_applications', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_career_office_coordinator


class StudentShowApplications(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/student_views_all_applications.html'
    context_object_name = 'student_views_all_applications'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


# here they can add, view progress reports
class StudentShowActiveInternship(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/student_view_active_internship.html'
    context_object_name = 'student_view_active_internship'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(StudentShowActiveInternship, self).get_context_data(**kwargs)
        # context['company_name'] = self.object_list[0].job_id.employer_id.company_name

        convo = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        if convo.exists():
            context['exists'] = True
        else:
            context['exists'] = False

        return context

    def test_func(self):
        return self.request.user.is_student


class StudentShowPastInternships(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/student_view_past_internships.html'
    context_object_name = 'student_view_past_internships'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


# class ShowAllJobsForStudent(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Job
#     template_name = 'portal/student_views_jobs.html'
#     context_object_name = 'student_views_jobs'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_student


# here the apply button
# class ShowJobForStudent(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Job
#     template_name = 'portal/student_views_job.html'
#     context_object_name = 'student_views_job'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_student


class StudentConfirmApply(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Application
    template_name = 'portal/student_apply_for_job.html'
    fields = ('confirm',)
    context_object_name = 'student_apply_for_job'
    login_url = 'login'
    success_url = 'successful_application'

    def get_success_url(self):
        pk = self.kwargs["pk"]

        return reverse('successful_application', kwargs={'pk': pk})

    def form_valid(self, form):
        student = models.Student(user=self.request.user)
        form.instance.student_id = student
        pk = self.kwargs["pk"]
        job = Job(pk=pk)
        form.instance.job_id = job
        # pass parameter of job when calling this view so make url take in primary key of job
        return super().form_valid(form)

    def test_func(self):
        # and job is visible for admin and faculty
        return self.request.user.is_student


class SuccessfulApplicationView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'portal/successful_application.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


class StudentShowProgressReports(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.Student
    template_name = 'portal/student_show_progress_reports.html'
    context_object_name = 'student_show_progress_reports'
    login_url = 'login'

    def get_queryset(self):
        std = models.Student(user=self.request.user)
        return ProgressReport.objects.filter(student_id=std)

    def get_context_data(self, **kwargs):
        context = super(StudentShowProgressReports, self).get_context_data(**kwargs)
        std = models.Student(user=self.request.user)
        reports = ProgressReport.objects.filter(student_id=std)
        context['reports'] = reports
        context['std'] = std
        return context

    def test_func(self):
        return self.request.user.is_student


class StudentShowProgressReport(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ProgressReport
    template_name = 'portal/student_show_progress_report.html'
    context_object_name = 'student_show_progress_report'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


class StudentFillInProgressReport(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProgressReport
    template_name = 'portal/student_fills_in_progress_report.html'
    fields = ('progress_report_title', 'progress_report_description', 'application_id')
    context_object_name = 'student_fills_in_progress_report'
    login_url = 'login'
    success_url = 'student_views_progress_reports'

    def form_valid(self, form):
        std = models.Student(user=self.request.user)
        form.instance.student_id = std
        job = form.cleaned_data['application_id']
        form.instance.academic_advisor_id = job.job_id.aa_id

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('student_views_progress_reports', kwargs={"pk": self.request.user.pk})

    def test_func(self):
        return self.request.user.is_student


class AcademicAdvisorShowAssignedStudents(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/acadamic_adv_view_assigned_internships.html'
    context_object_name = 'acadamic_adv_views_assigned_internships'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_academic_advisor


class AcademicAdvisorListProgressReports(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ProgressReport
    template_name = 'portal/acadamic_adv_views_progress_reports.html'
    context_object_name = 'acadamic_adv_views_progress_reports'
    login_url = 'login'

    def get_queryset(self):
        aa = models.AcademicAdvisor.objects.filter(user=self.request.user)[0]
        return ProgressReport.objects.filter(academic_advisor_id=aa)

    def test_func(self):
        return self.request.user.is_academic_advisor


class AcademicAdvisorViewProgressReport(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ProgressReport
    template_name = 'portal/acadamic_adv_read_progress_report.html'
    context_object_name = 'acadamic_adv_read_progress_report'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_academic_advisor


class AcademicAdvisorEvaluateProgressReport(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProgressReport
    fields = ('evaluation',)
    template_name = 'portal/academic_advisor_evaluates_progress_report.html'
    context_object_name = 'academic_advisor_evaluates_progress_report'
    login_url = 'login'
    success_url = 'academic_adv_list_progress_reports'

    def get_success_url(self):
        return reverse('academic_adv_list_progress_reports', kwargs={"pk": self.request.user.pk})

    def test_func(self):
        return self.request.user.is_academic_advisor


#
# class AcademicAdvisorViewsStudentJob(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Job
#     template_name = 'portal/academicadvisorviewsjob.html'
#     context_object_name = 'cademic_advisor_viewsjob'
#     login_url = 'login'
#
#     def test_func(self):
#         return self.request.user.is_academic_advisor


class StudentReadsEvaluation(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ProgressReport
    template_name = 'portal/studentreadsevaluation.html'
    context_object_name = 'student_reads_evaluatioon'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student
