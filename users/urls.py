from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.GenericSignUpView.as_view(), name='signup'),
    path('student/signup/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('employer/signup/', views.EmployerSignUpView.as_view(), name='employer_signup'),
    path('admin/signup/', views.GIUAdminSignUpView.as_view(), name='admin_signup'),
    path('facultyrepresentative/signup/', views.FacultyRepresentativeSignUpView.as_view(),
         name='faculty_representative_signup'),
    path('academicadvisor/signup/', views.AcademicAdvisorSignUpView.as_view(),
         name='academic_advisor_signup'),
    path('careerofficeecoordinator/signup/', views.CareerOfficeCoordinatorSignUpView.as_view(),
         name='career_office_coordinator_signup'),
    #     Edit urls
    path('student/<int:pk>/edit', views.StudentUpdateView.as_view(), name='student_edit'),
    path('employer/<int:pk>/edit', views.EmployerUpdateView.as_view(), name='employer_edit'),
    path('facultyrepresentative/<int:pk>/edit', views.FacultyRepresentativeUpdateView.as_view(), name='facrep_edit'),
    path('academicadvisor/<int:pk>/edit', views.AcademicAdvisorUpdateView.as_view(), name='acadadv_edit'),
    # Delete urls



]
