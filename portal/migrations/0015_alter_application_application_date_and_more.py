# Generated by Django 4.0 on 2022-01-04 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_job_active_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 20, 23, 44, 335542)),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='progress_report_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 20, 23, 44, 335542)),
        ),
    ]
