from django.urls import path, include
from portal import views

urlpatterns = [path('adminlistemployers/', views.ListEmployeesViewAdmin.as_view(), name='admin_list_employers'),
               path('adminlistemployers/delete', views.UserDeleteView.as_view(), name='admin_delete_employer'),
               path('adminlistemployers/changestatus', views.UpdateEmployerProfileStatus.as_view(),
                    name='update_profile_status'),
               path('adminlistfacrep/', views.ListFacRepAdmin.as_view(), name='list_fac_rep'),
               path('adminlistfacrep/delete/', views.UserDeleteView.as_view(), name='admin_delete_fac'),
               path('adminliststudent/', views.ListStudentsAdmin.as_view(), name='list_students_admin'),
               path('adminliststudent/delete/', views.UserDeleteView.as_view(), name='admin_delete_students'),
               path('adminlistacademicadvisor/', views.ListAcademicAdvisorAdmin.as_view(),
                    name='list_academic_advisor_admin'),
               path('adminlistacademicadvisor/delete/', views.UserDeleteView.as_view(),
                    name='admin_delete_academic_advisor'),
               path('adminlistcareeroc/', views.ListCareerOCAdmin.as_view(), name='list_career_oc_admin'),
               path('adminlistcareeroc/delete/', views.UserDeleteView.as_view(), name='admin_delete_career_oc_admin'),
               path('listjobs/', views.AdminShowJobs.as_view(), name='admin_views_jobs'),
               path('listjobs/changejobstatus', views.AdminChangeJobStatus.as_view(), name='admin_change_job_status'),

               # generic
               path('admin_view/generic/', include('portal.urls')),

               ]
