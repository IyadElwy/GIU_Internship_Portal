from django.urls import path, include
from portal import views

urlpatterns = [
    path('postjob/', views.EmployerPostsJobView.as_view(), name='employer_posts_job'),
    path('showpostedjobs/', views.ShowPostedJobsEmployerView.as_view(), name='employer_show_posted_jobs'),
    path('job_post_success/', views.EmployerJobPostSuccessful.as_view(), name='employer_job_post_successful'),
    path('profilenotaccepted/', views.EmployerStatusNotAccepted.as_view(),
         name='employer_status_not_accepted'),
]
