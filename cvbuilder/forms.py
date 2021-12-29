from django import forms
from django.forms import ModelForm
from .models import CvBuilder


class CreateResumeForm(ModelForm):
    linked_in_link = forms.CharField(max_length=30, required=False)
    github_link = forms.CharField(max_length=30, required=False)

    class Meta:
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
