# Generated by Django 4.0 on 2022-01-04 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_facultyrepresentative_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyrepresentative',
            name='d',
        ),
    ]
