from django.urls import path, include
from portal import views

urlpatterns = [
    path('applications/', views.StudentShowApplications.as_view(), name='student_show_applications'),
    path('activeinternships/', views.StudentShowActiveInternship.as_view(), name='student_show_active_internships'),
    path('pastinternships/', views.StudentShowPastInternships.as_view(), name='student_show_past_internships'),

]
