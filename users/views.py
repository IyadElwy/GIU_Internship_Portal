from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from . import models
from django.contrib.auth import login
from django.shortcuts import redirect


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


class GIUAdminSignUpView(CreateView):
    model = models.GIUAdmin
    form_class = forms.GIUAdminSignUpForm
    success_url = reverse_lazy('login')
    context_object_name = 'admin_signup_view'
    template_name = 'signup/admin_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class FacultyRepresentativeSignUpView(CreateView):
    model = models.FacultyRepresentative
    form_class = forms.FacultyRepresentativeForm
    success_url = reverse_lazy('login')
    context_object_name = 'facultyrepresentative_signup_view'
    template_name = 'signup/facultyrepresentative_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'facultyrepresentative'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class AcademicAdvisorSignUpView(CreateView):
    model = models.AcademicAdvisor
    form_class = forms.AcademicAdvisorForm
    success_url = reverse_lazy('login')
    context_object_name = 'academicadvisor_signup_view'
    template_name = 'signup/academicadvisor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'academicadvisor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class CareerOfficeCoordinatorSignUpView(CreateView):
    model = models.CareerOfficeCoordinator
    form_class = forms.CareerOfficeCoordinatorForm
    success_url = reverse_lazy('login')
    context_object_name = 'careerofficeecoordinator_signup_view'
    template_name = 'signup/careerofficeecoordinator_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'careerofficeecoordinator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
