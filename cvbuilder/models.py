from django.db import models
from users.models import Student
from django.conf import settings


class CvBuilder(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    personal_phone = models.CharField(max_length=30)
    personal_email = models.CharField(max_length=50)
    education = models.TextField(max_length=1000)
    extracurricular_activities = models.TextField(max_length=2000)
    skills = models.TextField(max_length=300)
    achievements = models.TextField(max_length=1000)
    languages = models.TextField(max_length=100)
    interests = models.TextField(max_length=300)
    experience = models.TextField(max_length=2000)
    linked_in_link = models.CharField(max_length=30, null=True)
    github_link = models.CharField(max_length=30, null=True)
    profile_image = models.ImageField(upload_to=str(settings.MEDIA_ROOT) + '/profile_images/', blank=True, null=True,
                                      default='profile_images/default.jpg', max_length=1000)

    def __str__(self):
        return f"CV: {self.student_id.user.first_name} {self.student_id.user.last_name}"

    def skills_as_list(self):
        return self.skills.split(';')

    def education_as_list(self):
        result_list = []
        split_by_education = self.education.split(';')[:-1]
        for education in split_by_education:
            split_by_detail = education.split(',')
            result_list.append([])
            for i, det in enumerate(split_by_detail):
                result_list[-1].append(split_by_detail[i])

        return result_list

    def experiences_as_list(self):
        result_list = []
        split_by_experience = self.experience.split(';')[:-1]
        for experience in split_by_experience:
            split_by_detail = experience.split(',')
            result_list.append([])
            for i, det in enumerate(split_by_detail):
                result_list[-1].append(split_by_detail[i])
        return result_list

    def achievements_as_list(self):
        result_list = []
        split_by_achievement = self.achievements.split(';')[:-1]
        for achievement in split_by_achievement:
            split_by_detail = achievement.split(',')
            result_list.append([])
            for i, det in enumerate(split_by_detail):
                result_list[-1].append(split_by_detail[i])
        return result_list

    def extracurricular_activities_as_list(self):
        result_list = []
        split_by_activity = self.extracurricular_activities.split(';')[:-1]
        for activity in split_by_activity:
            split_by_detail = activity.split(',')
            result_list.append([])
            for i, det in enumerate(split_by_detail):
                result_list[-1].append(split_by_detail[i])
        return result_list

    def languages_as_list(self):
        return self.languages.split(';')

    def interests_as_list(self):
        return self.interests.split(';')
