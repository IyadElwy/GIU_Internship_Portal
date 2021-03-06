# Generated by Django 4.0 on 2022-01-05 21:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='creator', serialize=False, to='users.user')),
                ('started_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(verbose_name='Confirm')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to='users.user')),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(max_length=500)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.conversation')),
                ('message_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
