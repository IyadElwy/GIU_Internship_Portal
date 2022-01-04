from django.urls import path, include
from . import views

urlpatterns = [
    # Signup urls
    path('student/signup/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('employer/signup/', views.EmployerSignUpView.as_view(), name='employer_signup'),
    path('giuadmin/signup/', views.GIUAdminSignUpView.as_view(), name='admin_signup'),
    path('facultyrepresentative/signup/', views.FacultyRepresentativeSignUpView.as_view(),
         name='faculty_representative_signup'),
    path('academicadvisor/signup/', views.AcademicAdvisorSignUpView.as_view(),
         name='academic_advisor_signup'),
    path('careerofficeecoordinator/signup/', views.CareerOfficeCoordinatorSignUpView.as_view(),
         name='career_office_coordinator_signup'),
    # View Profile urls
    path('student/<int:pk>/', views.StudentProfileView.as_view(), name='student_profile'),
    path('employer/<int:pk>/', views.EmployerProfileView.as_view(), name='employer_profile'),
    path('giuadmin/<int:pk>/', views.AdminProfileView.as_view(), name='admin_profile'),
    path('facultyrepresentative/<int:pk>/', views.FacultyRepresentativeProfileView.as_view(),
         name='facrep_profile'),
    path('academicadvisor/<int:pk>/', views.AcademicAdvisorProfileView.as_view(), name='acadadv_profile'),
    path('careerofficeecoordinator/<int:pk>/', views.CareerOfficeCoordinatorProfileView.as_view(),
         name='careerofc_profile'),

    #     Edit urls
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('employer/<int:pk>/edit/', views.EmployerUpdateView.as_view(), name='employer_edit'),

    path('employer/<int:pk>/contactperson/', views.ShowContactPerson.as_view(), name='contact_person'),
    path('employer/<int:pk>/contactperson/edit/', views.EditContactPerson.as_view(), name='contact_person_edit'),
    path('employer/<int:pk>/hrdirector/', views.ShowHRDirector.as_view(), name='hrdirector'),
    path('employer/<int:pk>/hrdirector/edit/', views.EditHRDirector.as_view(), name='hrdirector_edit'),

    path('facultyrepresentative/<int:pk>/edit/', views.FacultyRepresentativeUpdateView.as_view(), name='facrep_edit'),
    path('academicadvisor/<int:pk>/edit/', views.AcademicAdvisorUpdateView.as_view(), name='acadadv_edit'),
    # Delete urls
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='user_delete'),
    # successful signup
    path('signupsuccessful/', views.SuccessfulSignupView.as_view(), name='success_signup'),
    path('signupsuccessfulemployer/', views.SuccessfulSignupEmployerView.as_view(), name='success_signup_employer'),
    # resume
    path('student/<int:pk>/resume/', include('cvbuilder.urls')),

    path('student/<slug:pk>/phonenumbers/', views.StudentPhoneView.as_view(), name='student_phone_detail'),
    path('student/<slug:pk>/phonenumbers/add', views.AddStudentPhoneView.as_view(), name='add_student_phone'),
    path('student/<slug:pk>/phonenumbers/delete', views.DeleteStudentPhoneView.as_view(),
         name='delete_student_phone'),

    path('employer/<int:pk>/profilestatus/', views.EmployerProfileStatus.as_view(), name='employer_profile_status'),

    # portal
    path('employer/<int:pk>/employer_portal/', include('employer.urls')),
    path('giuadmin/<int:pk>/admin_portal/', include('giuadmin.urls')),
    path('student/<int:pk>/student_portal/', include('student.urls')),
    path('facultyrepresentative/<int:pk>/facrep_portal/', include('fac_rep.urls')),
    path('academicadvisor/<int:pk>/acadadv_portal/', include('acad_adv.urls')),
    path('careerofficeecoordinator/<int:pk>/careeroc_portal/', include('career_oc.urls')),

    # news
    path('giuadmin/<int:pk>/news/', include('news.urls')),
]
