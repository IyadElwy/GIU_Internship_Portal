from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import StudentSignUpForm
from . import models
from django.contrib.auth import login
from django.shortcuts import redirect


class StudentSignUpView(CreateView):
    model = models.Student
    form_class = StudentSignUpForm
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
