from django.urls import path, include
from portal import views

urlpatterns = [
    path('showassignedinternships/', views.AcademicAdvisorListProgressReports.as_view(),
         name='academic_adv_list_progress_reports'),
    path('showassignedinternships/readprogressreport/', views.AcademicAdvisorViewProgressReport.as_view(),
         name='academic_read_progress_report'),
    path('showassignedinternships/evaluatesprogressreport/', views.AcademicAdvisorEvaluateProgressReport.as_view(),
         name='academic_advisor_evaluates_progress_report'),

]
