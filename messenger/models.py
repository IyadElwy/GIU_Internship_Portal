import django.utils.timezone
from django.db import models
from users import models as user_models


class Conversation(models.Model):
    # convo_id = models.AutoField()
    user1 = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='creator', primary_key=True)
    user2 = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='created')
    started_on = models.DateTimeField(default=django.utils.timezone.now)
    active = models.BooleanField(verbose_name='Confirm')

    class Meta:
        unique_together = (('user1', 'user2'),)

    def __str__(self):
        return f'{self.user1.username}-{self.user2.username}'


class UserMessage(models.Model):
    msg_id = models.AutoField(primary_key=True)
    message_user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    date_time = models.DateTimeField(default=django.utils.timezone.now)
    conversation = models.ForeignKey(Conversation, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message_user.username}: {self.message}'
