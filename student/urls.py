from django.urls import path, include
from portal import views

urlpatterns = [
    path('applications/', views.StudentShowApplications.as_view(), name='student_show_applications'),
    path('activeinternships/', views.StudentShowActiveInternship.as_view(), name='student_show_active_internships'),
    path('activeinternships/addprogressreport/', views.StudentFillInProgressReport.as_view(),
         name='student_adds_progress_report'),
    path('viewprogressreports/', views.StudentShowProgressReports.as_view(),
         name='student_views_progress_reports'),
    path('viewprogressreports/addprogressreport/', views.StudentFillInProgressReport.as_view(),
         name='student_fills_in_report'),
    path('viewprogressreports/viewprogressreport/', views.StudentShowProgressReport.as_view(),
         name='student_views_progress_report'),
    path('viewprogressreports/viewevaluation/', views.StudentReadsEvaluation.as_view(),
         name='student_views_evaluation'),
    path('pastinternships/', views.StudentShowPastInternships.as_view(), name='student_show_past_internships'),
    path('apply/', views.StudentConfirmApply.as_view(), name='student_applies'),
    path('apply/successful/', views.SuccessfulApplicationView.as_view(), name='successful_application')

]
