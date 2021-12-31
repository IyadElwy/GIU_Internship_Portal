from django.urls import path, include
from portal import views
from cvbuilder.views import ShowResumeView

urlpatterns = [
    path('adminlistemployers/', views.ListEmployeesViewAdmin.as_view(), name='admin_list_employers'),
    path('adminlistemployers/delete', views.UserDeleteView.as_view(), name='admin_delete_employer'),
    path('adminlistemployers/changestatus', views.UpdateEmployerProfileStatus.as_view(), name='update_profile_status'),
    path('adminlistfacrep/', views.ListFacRepAdmin.as_view(), name='list_fac_rep'),
    path('adminlistfacrep/delete/', views.UserDeleteView.as_view(), name='admin_delete_fac'),
    path('adminliststudent/', views.ListStudentsAdmin.as_view(), name='list_students_admin'),
    path('adminliststudent/delete/', views.UserDeleteView.as_view(), name='admin_delete_students'),
    path('adminlistacademicadvisor/', views.ListAcademicAdvisorAdmin.as_view(), name='list_academic_advisor_admin'),
    path('adminlistacademicadvisor/delete/', views.UserDeleteView.as_view(), name='admin_delete_academic_advisor'),
    path('adminlistcareeroc/', views.ListCareerOCAdmin.as_view(), name='list_career_oc_admin'),
    path('adminlistcareeroc/delete/', views.UserDeleteView.as_view(), name='admin_delete_career_oc_admin'),
    path('employer/', views.EmployerProfileViewGeneric.as_view(), name='generic_employer_profile'),
    path('student/', views.StudentProfileViewGeneric.as_view(), name='generic_student_profile'),
    path('student/resume/', ShowResumeView.as_view(), name='generic_student_resume'),
    path('generic/contactperson/', views.ShowContactPersonGeneric.as_view(), name='generic_contact_person'),
    path('generic/hrdirector/', views.ShowHRDirectorGeneric.as_view(), name='generic_hr_director'),
    path('coclistacademicadvisor/', views.ListAcademicAdvisorCOC.as_view(), name='list_academic_advisor_coc'),

    path('', views.HomePageView.as_view(), name='home'),
]
