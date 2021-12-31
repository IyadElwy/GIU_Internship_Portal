from django.conf import settings
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users import models
from .models import ReviewProfile


class HomePageView(TemplateView):
    template_name = 'home.html'


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
