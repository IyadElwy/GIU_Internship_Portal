from django.db import models
from users.models import Student


class CvBuilder(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    personal_phone = models.CharField(max_length=30)
    personal_email = models.CharField(max_length=50)
    education = models.TextField(max_length=100)
    extracurricular_activities = models.TextField(max_length=300)
    skills = models.TextField(max_length=300)
    achievements = models.TextField(max_length=300)
    languages = models.TextField(max_length=100)
    interests = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    linked_in_link = models.CharField(max_length=30, null=True)
    github_link = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"CV: {self.student_id.user.first_name} {self.student_id.user.last_name}"
