from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import CvBuilder
from users.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from .forms import CreateResumeForm


class CVExample(TemplateView):
    template_name = 'cvbuilder/example.html'


class ResumeHomeView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'cvbuilder/resumehome.html'
    model = Student
    context_object_name = 'showResumeHomePageView'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student and self.request.user.pk == self.get_object().pk


class CreateResumeView(LoginRequiredMixin, CreateView):
    model = CvBuilder
    form_class = CreateResumeForm
    template_name = 'cvbuilder/createresume.html'
    success_url = reverse_lazy('resumehome')
    context_object_name = 'create_resume_view'
    login_url = 'login'

    def form_valid(self, form):
        Student.objects.filter(user=self.request.user).update(has_cv=True)
        student = Student(user=self.request.user)
        form.instance.student_id = student
        return super(CreateResumeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})


class EditResumeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CvBuilder
    fields = ('personal_phone',
              'personal_email',
              'education',
              'extracurricular_activities',
              'skills',
              'achievements',
              'languages',
              'interests',
              'experience',
              'linked_in_link',
              'github_link')
    template_name = 'cvbuilder/update_resume.html'
    context_object_name = 'resume_update_view'
    login_url = 'login'
    success_url = reverse_lazy('resumehome')

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        obj = self.get_object()
        return self.get_object().pk == self.request.user


class DeleteResumeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CvBuilder
    template_name = 'cvbuilder/delete_resume.html'
    context_object_name = 'resume_delete_view'
    success_url = reverse_lazy('resumehome')

    def form_valid(self, form):
        Student.objects.filter(user=self.request.user).update(has_cv=False)
        return super(DeleteResumeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        obj = self.get_object()
        return self.get_object().pk == self.request.user

# class ShowResumeView(DetailView)
