from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . import models


class StudentSignUpForm(UserCreationForm):
    middle_name = forms.CharField(max_length=20)

    student_university_id = forms.IntegerField()
    birthdate = forms.DateField()
    semester = forms.IntegerField()
    faculty = forms.CharField(max_length=20)
    major = forms.CharField(max_length=20)
    gpa = forms.DecimalField(decimal_places=3, max_digits=3)
    student_address = forms.CharField(max_length=10)
    cover_letter = forms.TextInput()

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('first_name', 'last_name', 'username', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = models.Student.objects.create(user=user, middle_name=self.data.get('middle_name'),
                                                student_university_id=self.data.get('student_university_id'),
                                                birthdate=self.data.get('birthdate'),
                                                semester=self.data.get('semester'),
                                                faculty=self.data.get('faculty'),
                                                major=self.data.get('major'),
                                                gpa=self.data.get('gpa'),
                                                student_address=self.data.get('student_address'),
                                                )

        return user
