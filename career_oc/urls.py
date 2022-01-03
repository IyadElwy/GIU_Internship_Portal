from django.urls import path, include
from portal import views

urlpatterns = [
    path('applications/', views.CocShowApplications.as_view(), name='coc_show_applications'),
    path('applications/updatevisibilty', views.CocUpdateStudentApplicationStatus.as_view(),
         name='coc_update_visibilty'),
    path('applications/assignaa', views.CocAssignsAcademicAdviserToJob.as_view(),
         name='coc_assigns_aa'),

]
