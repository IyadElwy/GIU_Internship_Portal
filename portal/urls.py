from django.urls import path, include
from portal import views
from cvbuilder.views import ShowResumeView

urlpatterns = [

    # generic
    path('employer/', views.EmployerProfileViewGeneric.as_view(), name='generic_employer_profile'),
    path('student/', views.StudentProfileViewGeneric.as_view(), name='generic_student_profile'),
    path('student/resume/', ShowResumeView.as_view(), name='generic_student_resume'),
    path('student/phones/', views.StudentPhoneViewGeneric.as_view(), name='generic_student_phone'),
    path('employer/contactperson/', views.ShowContactPersonGeneric.as_view(), name='generic_contact_person'),
    path('employer/hrdirector/', views.ShowHRDirectorGeneric.as_view(), name='generic_hr_director'),
    path('coclistacademicadvisor/', views.ListAcademicAdvisorCOC.as_view(), name='list_academic_advisor_coc'),
    path('viewjobs', views.ViewJobsGeneric.as_view(), name='generic_job_view'),
    path('viewjobs/job', views.GenericJobView.as_view(), name='job_generic'),
    path('messages/', include('messenger.urls')),

    # homepage
    path('', views.HomePageView.as_view(), name='home'),
    path('companies/', views.ShowCompanies.as_view(), name='allcompanies'),
    path('help/', views.HelpPageView.as_view(), name='help'),

]
