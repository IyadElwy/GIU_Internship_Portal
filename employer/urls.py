from django.urls import path, include
from portal import views

urlpatterns = [
    path('postjob/', views.EmployerPostsJobView.as_view(), name='employer_posts_job'),
    path('showpostedjobs/', views.ShowPostedJobsEmployerView.as_view(), name='employer_show_posted_jobs'),
    path('showpostedjobs/viewJob/', views.ShowJobForEmployer.as_view(), name='employer_show_job'),
    path('showpostedjobs/editjob/', views.EmployerUpdateJob.as_view(), name='employer_edits_job'),
    path('showpostedjobs/editjobvisibility/', views.EmployerUpdateJobVisibility.as_view(),
         name='employer_edits_job_visibility'),
    path('job_post_success/', views.EmployerJobPostSuccessful.as_view(), name='employer_job_post_successful'),
    path('profilenotaccepted/', views.EmployerStatusNotAccepted.as_view(),
         name='employer_status_not_accepted'),
    path('applications/', views.ShowAllApplicationsByCompany.as_view(), name='employer_show_applicationsByComp'),
    path('activeinternships/', views.EmployerShowAllActiveInternships.as_view(),
         name='employer_show_activeInternships'),
    path('activeinternships/endinternship', views.EmployerEndInternship.as_view(),
         name='employer_ends_internship'),
    path('applications/updatestatus', views.EmployerChangesStudentApplicationStatus.as_view(),
         name='employer_changes_application_status'),
    path('paystudents/', views.EmployerPayStudentForInternship.as_view(), name='employer_pays_students'),
    path('paystudents/payment', views.PaymentView.as_view(), name='payment'),

]
