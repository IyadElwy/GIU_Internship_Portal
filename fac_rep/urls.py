from django.urls import path, include
from portal import views

urlpatterns = [

    path('showjobs/', views.FacRepShowJobs.as_view(), name='fac_rep_views_jobs'),
    path('showjobs/changestatus', views.FacRepChangeJobStatus.as_view(), name='fac_rep_change_job_status'),

    # generic
    path('generic/', include('portal.urls')),

]
