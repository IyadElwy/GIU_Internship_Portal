# Generated by Django 4.0 on 2022-01-04 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_student_current_aa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='current_aa',
        ),
    ]
