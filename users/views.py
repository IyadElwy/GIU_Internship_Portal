from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView, ListView
from . import forms
from . import models
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from portal.models import ReviewProfile


class SuccessfulSignupView(TemplateView):
    template_name = 'signup/successful_signup_others.html'


class SuccessfulSignupEmployerView(TemplateView):
    template_name = 'signup/successful_signup_employer.html'


class StudentSignUpView(CreateView):
    model = models.Student
    form_class = forms.StudentSignUpForm
    success_url = reverse_lazy('success_signup')
    context_object_name = 'student_signup_view'
    template_name = 'signup/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup')


class EmployerSignUpView(CreateView):
    model = models.Employer
    form_class = forms.EmployerSignUpForm
    success_url = reverse_lazy('success_signup_employer')
    context_object_name = 'employer_signup_view'
    template_name = 'signup/employer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup_employer')


class GIUAdminSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.GIUAdmin
    form_class = forms.GIUAdminSignUpForm
    success_url = reverse_lazy('success_signup')
    context_object_name = 'admin_signup_view'
    template_name = 'signup/admin_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup')

    def test_func(self):
        return self.request.user.is_admin


class FacultyRepresentativeSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.FacultyRepresentative
    form_class = forms.FacultyRepresentativeForm
    success_url = reverse_lazy('success_signup')
    context_object_name = 'facultyrepresentative_signup_view'
    template_name = 'signup/facultyrepresentative_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'facultyrepresentative'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup')

    def test_func(self):
        return self.request.user.is_admin


class AcademicAdvisorSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.AcademicAdvisor
    form_class = forms.AcademicAdvisorForm
    success_url = reverse_lazy('success_signup')
    context_object_name = 'academicadvisor_signup_view'
    template_name = 'signup/academicadvisor_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'academicadvisor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup')

    def test_func(self):
        return self.request.user.is_admin


class CareerOfficeCoordinatorSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.CareerOfficeCoordinator
    form_class = forms.CareerOfficeCoordinatorForm
    success_url = reverse_lazy('success_signup')
    context_object_name = 'careerofficeecoordinator_signup_view'
    template_name = 'signup/careerofficeecoordinator_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'careerofficeecoordinator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('success_signup')

    def test_func(self):
        return self.request.user.is_admin


# Edit and Delete User Views


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Student
    fields = ('student_address',
              'semester',
              'faculty',
              'major',
              'gpa',
              'cover_letter')
    template_name = 'editusers/student_edit.html'
    context_object_name = 'student_edit_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student and self.request.user.pk == self.get_object().pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('student_profile', kwargs={"pk": pk})


class EmployerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Employer
    fields = ('company_name',
              'employer_address',
              'phone_number',
              'fax_number',
              'website',
              'type_of_business',
              'industry',
              'number_of_current_employees',
              'products_or_services',
              'company_logo')
    template_name = 'editusers/employer_edit.html'
    context_object_name = 'employer_edit_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer and self.request.user.pk == self.get_object().pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('employer_profile', kwargs={"pk": pk})


class FacultyRepresentativeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.FacultyRepresentative
    fields = ('faculty',)
    template_name = 'editusers/facultyrep_edit.html'
    context_object_name = 'facultyrep_edit_view'

    def test_func(self):
        return self.request.user.is_faculty_representative and self.request.user.pk == self.get_object().pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('facrep_profile', kwargs={"pk": pk})


class AcademicAdvisorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.AcademicAdvisor
    fields = ('faculty',)
    template_name = 'editusers/academicadv_edit.html'
    context_object_name = 'academicadv_edit_view'

    def test_func(self):
        return self.request.user.is_academic_advisor and self.request.user.pk == self.get_object().pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('acadadv_profile', kwargs={"pk": pk})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.User
    template_name = 'editusers/user_delete.html'
    context_object_name = 'user_delete_view'
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


# User profile views (if user views their own profile)
class StudentProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Student
    template_name = 'userprofiles/student_profile.html'
    context_object_name = 'student_profile_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class StudentPhoneView(LoginRequiredMixin, ListView):
    model = models.StudentPhoneNumbers
    template_name = 'userprofiles/student_phone_numbers.html'
    context_object_name = 'student_phone_list'
    login_url = 'login'


class AddStudentPhoneView(LoginRequiredMixin, CreateView):
    model = models.StudentPhoneNumbers
    fields = ('phone_number',)
    template_name = 'userprofiles/student_phone_numbers_add.html'
    context_object_name = 'create_phone_number'
    login_url = 'login'
    success_url = reverse_lazy('student_profile')

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('student_profile', kwargs={"pk": pk})

    def form_valid(self, form):
        student = models.Student(user=self.request.user)
        form.instance.student_id = student
        return super().form_valid(form)


class DeleteStudentPhoneView(LoginRequiredMixin, DeleteView):
    model = models.StudentPhoneNumbers
    template_name = 'userprofiles/student_delete_number.html'
    context_object_name = 'delete_phone_number'
    login_url = 'login'
    success_url = reverse_lazy('student_profile')

    def get_success_url(self):
        return reverse('student_profile', kwargs={"pk": self.request.user.pk})


class EmployerProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Employer
    api_key = settings.GOOGLE_MAPS_API_KEY
    api_key_places = settings.POSITION_API
    template_name = 'userprofiles/employer_profile.html'
    context_object_name = 'employer_profile_view'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(EmployerProfileView, self).get_context_data(**kwargs)
        context['google_maps_api_key'] = self.api_key
        context['positions_api_key'] = self.api_key_places
        return context

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class AdminProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.GIUAdmin
    template_name = 'userprofiles/admin_profile.html'
    context_object_name = 'admin_profile_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class FacultyRepresentativeProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.FacultyRepresentative
    template_name = 'userprofiles/facultyrep_profile.html'
    context_object_name = 'facultyrep_profile_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class AcademicAdvisorProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.AcademicAdvisor
    template_name = 'userprofiles/academicadv_profile.html'
    context_object_name = 'acadadv_profile_view'

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class CareerOfficeCoordinatorProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.CareerOfficeCoordinator
    template_name = 'userprofiles/careerofc_profile.html'
    context_object_name = 'careerofc_profile_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class EmployerProfileStatus(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ReviewProfile
    template_name = 'userprofiles/employer_status.html'
    context_object_name = 'employer_profile_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().employer_id.pk


class ShowContactPerson(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.ContactPerson
    template_name = 'userprofiles/show_contact_person.html'
    context_object_name = 'contact_person_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().employer_id.pk


class EditContactPerson(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.ContactPerson
    fields = ('contact_person_name', 'job_title', 'email', 'mobile_number')
    template_name = 'userprofiles/contact_person_edit.html'
    context_object_name = 'contact_person_edit_view'
    success_url = 'employer_profile'

    def test_func(self):
        return self.request.user.pk == self.get_object().employer_id.pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('employer_profile', kwargs={"pk": pk})


class ShowHRDirector(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.HRDirector
    template_name = 'userprofiles/show_hr_directore.html'
    context_object_name = 'hr_director_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.pk == self.get_object().employer_id.pk


class EditHRDirector(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.HRDirector
    fields = ('hr_name', 'hr_email')
    template_name = 'userprofiles/hr_director_edit.html'
    context_object_name = 'hr_director_edit_view'
    success_url = 'employer_profile'

    def test_func(self):
        return self.request.user.pk == self.get_object().employer_id.pk

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('employer_profile', kwargs={"pk": pk})
