from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.GenericSignUpView.as_view(), name='signup'),
    path('signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/employer/', views.EmployerSignUpView.as_view(), name='employer_signup'),
    path('signup/admin/', views.GIUAdminSignUpView.as_view(), name='admin_signup'),
    path('signup/facultyrepresentative/', views.FacultyRepresentativeSignUpView.as_view(),
         name='faculty_representative_signup'),
    path('signup/academicadvisor/', views.AcademicAdvisorSignUpView.as_view(),
         name='academic_advisor_signup'),
    path('signup/careerofficeecoordinator/', views.CareerOfficeCoordinatorSignUpView.as_view(),
         name='career_office_coordinator_signup'),

]
