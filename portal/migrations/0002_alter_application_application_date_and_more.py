# Generated by Django 4.0 on 2022-01-03 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 10, 57, 40, 190047)),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='progress_report_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 10, 57, 40, 190047)),
        ),
    ]