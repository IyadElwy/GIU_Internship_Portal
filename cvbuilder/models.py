from django.db import models
from users.models import Student


class CvBuilder(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.DO_NOTHING)
    personal_phone = models.CharField(max_length=30)
    personal_email = models.CharField(max_length=50)
    education = models.TextField(max_length=100)
    extracurricular_activities = models.TextField(max_length=300)
    skills = models.TextField(max_length=300)
    achievements = models.TextField(max_length=300)
    languages = models.TextField(max_length=100)
    interests = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    linked_in_link = models.CharField(max_length=30)
    github_link = models.CharField(max_length=30)

    def __str__(self):
        return f"CV: {self.student_id.first_name} {self.student_id.last_name}"
