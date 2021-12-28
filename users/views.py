from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import forms
from . import models
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StudentSignUpView(CreateView):
    model = models.Student
    form_class = forms.StudentSignUpForm
    success_url = reverse_lazy('login')
    context_object_name = 'student_signup_view'
    template_name = 'signup/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class EmployerSignUpView(CreateView):
    model = models.Employer
    form_class = forms.EmployerSignUpForm
    success_url = reverse_lazy('login')
    context_object_name = 'employer_signup_view'
    template_name = 'signup/employer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class GIUAdminSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.GIUAdmin
    form_class = forms.GIUAdminSignUpForm
    success_url = reverse_lazy('login')
    context_object_name = 'admin_signup_view'
    template_name = 'signup/admin_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

    def test_func(self):
        return self.request.user.is_admin


class FacultyRepresentativeSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.FacultyRepresentative
    form_class = forms.FacultyRepresentativeForm
    success_url = reverse_lazy('login')
    context_object_name = 'facultyrepresentative_signup_view'
    template_name = 'signup/facultyrepresentative_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'facultyrepresentative'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

    def test_func(self):
        return self.request.user.is_admin


class AcademicAdvisorSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.AcademicAdvisor
    form_class = forms.AcademicAdvisorForm
    success_url = reverse_lazy('login')
    context_object_name = 'academicadvisor_signup_view'
    template_name = 'signup/academicadvisor_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'academicadvisor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

    def test_func(self):
        return self.request.user.is_admin


class CareerOfficeCoordinatorSignUpView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.CareerOfficeCoordinator
    form_class = forms.CareerOfficeCoordinatorForm
    success_url = reverse_lazy('login')
    context_object_name = 'careerofficeecoordinator_signup_view'
    template_name = 'signup/careerofficeecoordinator_signup.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'careerofficeecoordinator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

    def test_func(self):
        return self.request.user.is_admin


# Edit and Delete User Views


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Student
    fields = ('student_address',
              'semester',
              'faculty',
              'major',
              'gpa',)
    template_name = 'editusers/student_edit.html'
    context_object_name = 'student_edit_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student and self.request.user == self.object.user


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
              'products_or_services')
    template_name = 'editusers/employer_edit.html'
    context_object_name = 'employer_edit_view'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_employer and self.request.user == self.object.user


class FacultyRepresentativeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.FacultyRepresentative
    fields = ('faculty',)
    template_name = 'editusers/facultyrep_edit.html'
    context_object_name = 'facultyrep_edit_view'

    def test_func(self):
        return self.request.user.is_faculty_representative and self.request.user == self.object.user


class AcademicAdvisorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.AcademicAdvisor
    fields = ('faculty',)
    template_name = 'editusers/academicadv_edit.html'
    context_object_name = 'academicadv_edit_view'

    def test_func(self):
        return self.request.user.is_academic_advisor and self.request.user == self.object.user


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.User
    template_name = 'editusers/user_delete.html'
    context_object_name = 'user_delete_view'
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user == self.object.user


# User profile views (if user views their own profile)
class StudentProfileView(LoginRequiredMixin, DetailView):
    model = models.Student
    template_name = 'userprofiles/student_profile.html'
    context_object_name = 'student_profile_view'
    login_url = 'login'


class EmployerProfileView(LoginRequiredMixin, DetailView):
    model = models.Employer
    template_name = 'userprofiles/employer_profile.html'
    context_object_name = 'employer_profile_view'
    login_url = 'login'


class AdminProfileView(LoginRequiredMixin, DetailView):
    model = models.GIUAdmin
    template_name = 'userprofiles/admin_profile.html'
    context_object_name = 'admin_profile_view'
    login_url = 'login'


class FacultyRepresentativeProfileView(LoginRequiredMixin, DetailView):
    model = models.FacultyRepresentative
    template_name = 'userprofiles/facultyrep_profile.html'
    context_object_name = 'facultyrep_profile_view'
    login_url = 'login'


class AcademicAdvisorProfileView(LoginRequiredMixin, DetailView):
    model = models.AcademicAdvisor
    template_name = 'userprofiles/academicadv_profile.html'
    context_object_name = 'acadadv_profile_view'


class CareerOfficeCoordinatorProfileView(LoginRequiredMixin, DetailView):
    model = models.CareerOfficeCoordinator
    template_name = 'userprofiles/careerofc_profile.html'
    context_object_name = 'careerofc_profile_view'
    login_url = 'login'
