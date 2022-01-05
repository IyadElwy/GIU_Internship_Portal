from django.urls import path, include
from . import views

urlpatterns = [

    path('createconversationstudent/<str:pk>/', views.StartConversationWithStudentView.as_view(),
         name='start_convo_student'),
    path('allmessages/', views.MessageHomeView.as_view(), name='message_home_page'),
    path('allmessages/<int:pk>/', views.ViewConversation.as_view(), name='view_convo_page'),
    path('allmessages/<int:pk>/createnewmessage/', views.SendNewMessage.as_view(),
         name='send_new_message_page'),

]
