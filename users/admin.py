import inspect

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models


class SuperUser(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_staff']


admin.site.register(User, SuperUser)
admin.site.register(models.GIUAdmin)
admin.site.register(models.Student)
admin.site.register(models.StudentPhoneNumbers)
admin.site.register(models.Employer)
admin.site.register(models.FacultyRepresentative)
admin.site.register(models.AcademicAdvisor)
admin.site.register(models.ContactPerson)
admin.site.register(models.HRDirector)
admin.site.register(models.IndustrialInternship)
admin.site.register(models.CvBuilder)
admin.site.register(models.Application)
admin.site.register(models.Eligible)
admin.site.register(models.ProgressReport)
admin.site.register(models.Job)
admin.site.register(models.CareerOfficeCoordinator)
