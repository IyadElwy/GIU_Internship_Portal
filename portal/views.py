import datetime

from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users import models
from .models import ReviewProfile, Job, ProgressReport, Application


class HomePageView(TemplateView):
    template_name = 'home.html'


class HelpPageView(TemplateView):
    template_name = 'help.html'


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
    login_url = 'login'

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
        std = models.Student(user=self.request.user)
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
        employer = models.Employer(user=self.request.user)
        return employer.reviewprofile.review_status == 'Accepted'


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

    def test_func(self):
        return self.request.user.is_employer


class ShowJobForEmployer(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = 'portal/employer_views_own_job.html'
    context_object_name = 'employer_views_own_jobs'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer and self.get_object().user == self.request.user


class ShowAllApplicationsByCompany(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_views_all_applications_by_company.html'
    context_object_name = 'employer_views_all_applications_by_company'
    login_url = 'login'
    queryset = Application.objects.order_by('application_date')

    def get_context_data(self, **kwargs):
        context = super(ShowAllApplicationsByCompany, self).get_context_data(**kwargs)
        context['company_name'] = self.object_list[0].job_id.employer_id.company_name
        return context

    def test_func(self):
        return self.request.user.is_employer


class ShowAllApplicationsByJob(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_views_all_applications_by_job.html'
    context_object_name = 'employer_views_all_applications_by_job'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer


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
            ProgressReport.objects.create(student_id=self.object.student_id,
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
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_employer


class EmployerPayStudentForInternship(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/employer_pay_for_internship.html'
    context_object_name = 'employer_pay_for_internship'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer


class PaymentView(TemplateView):
    template_name = 'portal/payment.html'
    context_object_name = 'employer_pay'


class AdminShowJobs(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/admin_views_all_jobs.html'
    context_object_name = 'admin_views_all_jobs'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class ShowJobForAdmin(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = 'portal/admin_views_job.html'
    context_object_name = 'admin_views_job'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_admin


class AdminChangeJobStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = 'portal/admin_change_job_status.html'
    fields = ('visibility_admin',)
    context_object_name = 'admin_change_job_status'
    login_url = 'login'
    success_url = reverse_lazy('admin_view_all_jobs')

    def get_success_url(self):
        return reverse('admin_view_all_jobs', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_admin


class FacRepShowJobs(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/fac_rep_show_jobs.html'
    context_object_name = 'fac_rep_show_jobs'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_faculty_representative


class ShowJobForFacRep(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = 'portal/fac_rep_views_job.html'
    context_object_name = 'fac_rep_views_job'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_faculty_representative


class FacRepChangeJobStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = 'portal/fac_rep_changes_job_status'
    fields = ('visibility_fac_rep',)
    context_object_name = 'fac_rep_changes_job_status'
    login_url = 'login'
    success_url = reverse_lazy('facrep_view_all_jobs')

    def get_success_url(self):
        return reverse('facrep_view_all_jobs', args=[self.request.user.pk])

    def test_func(self):
        return self.request.user.is_faculty_representative


class CocShowApplications(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/coc_views_application.html'
    context_object_name = 'coc_views_application'
    login_url = 'login'

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

    def test_func(self):
        return self.request.user.is_student


class StudentShowPastInternships(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'portal/student_view_past_internships.html'
    context_object_name = 'student_view_past_internships'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


class ShowAllJobsForStudent(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'portal/student_views_jobs.html'
    context_object_name = 'student_views_jobs'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


# here the apply button
class ShowJobForStudent(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = 'portal/student_views_job.html'
    context_object_name = 'student_views_job'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student


class StudentConfirmApply(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Application
    template_name = 'portal/student_apply_for_job.html'
    context_object_name = 'student_apply_for_job'
    login_url = 'login'

    def form_valid(self, form):
        student = models.Student(user=self.request.user)
        form.instance.student_id = student
        # pass parameter of job when calling this view so make url take in primary key of job
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_student


class StudentShowProgressReports(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.Student
    template_name = 'portal/student_show_progress_reports.html'
    context_object_name = 'student_show_progress_reports'
    login_url = 'login'

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
    fields = ('progress_report_title', 'progress_report_description', 'numeric_state')
    context_object_name = 'student_fills_in_progress_report'
    login_url = 'login'
    success_url = 'student_views_progress_reports'

    def form_valid(self, form):
        std = models.Student(user=self.request.user)
        form.instance.student_id = std
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


class StudentReadsEvaluation(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ProgressReport
    template_name = 'portal/studentreadsevaluation.html'
    context_object_name = 'student_reads_evaluatioon'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student
