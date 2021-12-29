from django.urls import path, include
from . import views

urlpatterns = [
    # Signup urls
    path('student/signup/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('employer/signup/', views.EmployerSignUpView.as_view(), name='employer_signup'),
    path('admin/signup/', views.GIUAdminSignUpView.as_view(), name='admin_signup'),
    path('facultyrepresentative/signup/', views.FacultyRepresentativeSignUpView.as_view(),
         name='faculty_representative_signup'),
    path('academicadvisor/signup/', views.AcademicAdvisorSignUpView.as_view(),
         name='academic_advisor_signup'),
    path('careerofficeecoordinator/signup/', views.CareerOfficeCoordinatorSignUpView.as_view(),
         name='career_office_coordinator_signup'),
    # View Profile urls
    path('student/<int:pk>/', views.StudentProfileView.as_view(), name='student_profile'),
    path('employer/<int:pk>/', views.EmployerProfileView.as_view(), name='employer_profile'),
    path('admin/<int:pk>/', views.AdminProfileView.as_view(), name='admin_profile'),
    path('facultyrepresentative/<int:pk>/', views.FacultyRepresentativeProfileView.as_view(),
         name='facrep_profile'),
    path('academicadvisor/<int:pk>/', views.AcademicAdvisorProfileView.as_view(), name='acadadv_profile'),
    path('careerofficeecoordinator/<int:pk>/', views.CareerOfficeCoordinatorProfileView.as_view(),
         name='careerofc_profile'),

    #     Edit urls
    path('student/<int:pk>/edit', views.StudentUpdateView.as_view(), name='student_edit'),
    path('employer/<int:pk>/edit', views.EmployerUpdateView.as_view(), name='employer_edit'),
    path('facultyrepresentative/<int:pk>/edit', views.FacultyRepresentativeUpdateView.as_view(), name='facrep_edit'),
    path('academicadvisor/<int:pk>/edit', views.AcademicAdvisorUpdateView.as_view(), name='acadadv_edit'),
    # Delete urls
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='user_delete'),
    # successful signup
    path('signupsuccessful/', views.SuccessfulSignupView.as_view(), name='success_signup'),
    path('signupsuccessfulemployer/', views.SuccessfulSignupEmployerView.as_view(), name='success_signup_employer'),
    # resume
    path('student/<int:pk>/resume/', include('cvbuilder.urls')),

]
