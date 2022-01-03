from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import CvBuilder
from users.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .forms import CreateResumeForm, EditResumeForm


class CVExample(TemplateView):
    template_name = 'cvbuilder/example.html'


class ResumeHomeView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'cvbuilder/resumehome.html'
    model = Student
    context_object_name = 'showResumeHomePageView'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_student and self.request.user.pk == self.get_object().pk


class CreateResumeView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        student = Student(user=self.request.user)
        return student.has_cv == False


class EditResumeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CvBuilder
    form_class = EditResumeForm
    template_name = 'cvbuilder/update_resume.html'
    context_object_name = 'resume_update_view'
    login_url = 'login'
    success_url = reverse_lazy('resumehome')

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        return self.get_object().student_id.user.pk == self.request.user.pk

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, student_id=self.kwargs['pk'])


class DeleteResumeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CvBuilder
    template_name = 'cvbuilder/delete_resume.html'
    context_object_name = 'resume_delete_view'
    success_url = reverse_lazy('resumehome')
    login_url = 'login'

    def form_valid(self, form):
        Student.objects.filter(user=self.request.user).update(has_cv=False)
        return super(DeleteResumeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        return self.get_object().student_id.user.pk == self.request.user.pk

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, student_id=self.kwargs['pk'])


class ShowResumeView(LoginRequiredMixin, DetailView):
    model = CvBuilder
    template_name = 'cvbuilder/show_resume.html'
    context_object_name = 'resume_show_view'
    success_url = reverse_lazy('resumehome')
    login_url = 'login'

    def get_success_url(self):
        return reverse('resumehome', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, student_id=self.kwargs['pk'])
