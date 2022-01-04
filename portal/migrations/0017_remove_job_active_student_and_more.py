# Generated by Django 4.0 on 2022-01-04 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_progressreport_academic_advisor_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='active_student',
        ),
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 21, 6, 50, 365930)),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='progress_report_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 21, 6, 50, 365930)),
        ),
    ]
