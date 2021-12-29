from django.urls import path
from .views import ResumeHomeView, CreateResumeView, EditResumeView, DeleteResumeView

urlpatterns = [
    path('', ResumeHomeView.as_view(), name='resumehome'),
    path('create/', CreateResumeView.as_view(), name='createresume'),
    path('edit/', EditResumeView.as_view(), name='editresume'),
    # path('show/', ShowResumeHome.as_view(), name='showresume'),
    path('delete/', DeleteResumeView.as_view(), name='deleteresume'),
]
