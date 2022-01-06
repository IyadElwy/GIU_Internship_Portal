from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from users.models import Student, User
from django.db.models import Q


class MessageHomeView(LoginRequiredMixin, ListView):
    model = models.Conversation
    template_name = 'messanger/messagehomepage.html'
    context_object_name = 'conversation_list_view'
    login_url = 'login'

    def get_queryset(self):
        return models.Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))


class StartConversationWithStudentView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Conversation
    fields = ('active',)
    template_name = 'messanger/confirmconvostudent.html'
    context_object_name = 'start_convo_student_view'
    login_url = 'login'
    success_url = reverse_lazy('message_home_page')

    def get_success_url(self):
        return reverse('message_home_page', args=[self.request.user.pk])

    def form_valid(self, form):
        start_user = self.request.user
        user2username = self.kwargs['pk']
        user2 = User.objects.filter(username=user2username)[0]
        form.instance.user1 = start_user
        form.instance.user2 = user2
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_academic_advisor or self.request.user.is_employer or \
               self.request.user.is_faculty_representative or self.request.user.is_admin or \
               self.request.user.is_career_office_coordinator or self.request.user


class ViewConversation(LoginRequiredMixin, ListView):
    model = models.UserMessage
    template_name = 'messanger/viewmessages.html'
    context_object_name = 'message_list_view'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewConversation, self).get_context_data(**kwargs)
        user1 = self.kwargs['pk1']
        user2 = self.kwargs['pk2']
        convo = models.Conversation.objects.filter(user1=user1, user2=user2)[0]
        context["conversation"] = convo
        return context

    def get_queryset(self):
        user1 = self.kwargs['pk1']
        user2 = self.kwargs['pk2']
        convo = models.Conversation.objects.filter(user1=user1, user2=user2)[0]
        return models.UserMessage.objects.filter(conversation=convo).order_by('-date_time')


class SendNewMessage(LoginRequiredMixin, CreateView):
    model = models.UserMessage
    template_name = 'messanger/writenewmessage.html'
    context_object_name = 'write_new_message'
    login_url = 'login'
    fields = ('message',)
    success_url = 'message_home_page'

    def get_success_url(self):
        return reverse('message_home_page', args=[self.request.user.pk])

    def form_valid(self, form):
        form.instance.message_user = self.request.user
        user1 = self.kwargs['pk1']
        user2 = self.kwargs['pk2']
        convo = models.Conversation.objects.filter(user1=user1, user2=user2)[0]
        form.instance.conversation = convo

        return super().form_valid(form)

#
# class StartConversationWithEmployerView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = models.Conversation
#     fields = ('active',)
#     template_name = 'messanger/confirmconvo.html'
#     context_object_name = 'start_convo_view'
#     login_url = 'login'
#     success_url = reverse_lazy('')
#
#     def get_success_url(self):
#         return reverse('', args=[self.request.user.pk])
#
#     def form_valid(self, form):
#         start_user = self.request.user
#
#         form.instance.employer_id = employer
#         return super().form_valid(form)
#
#     def test_func(self):
#         return None
