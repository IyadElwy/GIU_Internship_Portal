# Generated by Django 4.0 on 2021-12-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0002_alter_cvbuilder_github_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvbuilder',
            name='achievements',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cvbuilder',
            name='education',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cvbuilder',
            name='experience',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='cvbuilder',
            name='extracurricular_activities',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='cvbuilder',
            name='interests',
            field=models.TextField(max_length=300),
        ),
    ]
