from django import forms
from django.forms import ModelForm
from .models import CvBuilder


class CreateResumeForm(ModelForm):
    linked_in_link = forms.CharField(max_length=30, required=False)
    github_link = forms.CharField(max_length=30, required=False)

    education = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'School certificate type,\nSchool Name,'
                                                                            '\nEducation type,'
                                                                            '\nTime;\nSchool certificate type,'
                                                                            '\nSchool Name,\nEducation '
                                                                            'type,\nTime;'}))
    extracurricular_activities = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Title,\nDescription;\nTitle,\nDescription;'}))
    skills = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'skill1;skill2;skill3;etc;'}))
    achievements = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Title,\nDescription;'}))
    languages = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'language1;language2;language3;etc;'}))
    interests = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'interest1;interest2;interest3;etc;'}))
    experience = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Title,\nPlace and Time,\nDescription;\nTitle,\nPlace and Time,\nDescription;'}))

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
                  'github_link',
                  'profile_image')


class EditResumeForm(ModelForm):
    linked_in_link = forms.CharField(max_length=30, required=False)
    github_link = forms.CharField(max_length=30, required=False)

    education = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'School certificate type,\nSchool Name,'
                                                                            '\nEducation type,'
                                                                            '\nTime;\nSchool certificate type,'
                                                                            '\nSchool Name,\nEducation '
                                                                            'type,\nTime;'}))
    extracurricular_activities = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Title,\nDescription;\nTitle,\nDescription;'}))
    skills = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'skill1;skill2;skill3;etc;'}))
    achievements = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Title,\nDescription;'}))
    languages = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'language1;language2;language3;etc;'}))
    interests = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'interest1;interest2;interest3;etc;'}))
    experience = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Title,\nPlace and Time,\nDescription;\nTitle,\nPlace and Time,\nDescription;'}))

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
                  'github_link',
                  'profile_image')
