from django.urls import path
from .views import ResumeHomeView, CreateResumeView, EditResumeView, DeleteResumeView, ShowResumeView

urlpatterns = [
                  path('create/', CreateResumeView.as_view(), name='createresume'),
                  path('edit/', EditResumeView.as_view(), name='editresume'),
                  path('show/', ShowResumeView.as_view(), name='showresume'),
                  path('delete/', DeleteResumeView.as_view(), name='deleteresume'),
                  path('', ResumeHomeView.as_view(), name='resumehome'),

              ]
