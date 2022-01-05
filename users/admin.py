import inspect

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models
from portal import models as portal_models
from cvbuilder import models as cv_models
from news.models import Article
from messenger.models import Conversation, UserMessage

admin.site.site_header = 'GIU Internship Portal'
admin.site.index_title = 'GIU IP Admin'


class SuperUser(UserAdmin):
    model = User
    list_display = ['pk', 'email', 'username', 'is_staff']


admin.site.register(User, SuperUser)
admin.site.register(models.GIUAdmin)
admin.site.register(models.Student)
admin.site.register(models.CareerOfficeCoordinator)
admin.site.register(models.StudentPhoneNumbers)
admin.site.register(models.Employer)
admin.site.register(models.FacultyRepresentative)
admin.site.register(models.AcademicAdvisor)
admin.site.register(models.ContactPerson)
admin.site.register(models.HRDirector)

admin.site.register(portal_models.Application)
admin.site.register(portal_models.ProgressReport)
admin.site.register(portal_models.Job)
admin.site.register(portal_models.ReviewProfile)

admin.site.register(cv_models.CvBuilder)

admin.site.register(Article)
# messanger
admin.site.register(UserMessage)
admin.site.register(Conversation)
