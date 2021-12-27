# Generated by Django 4.0 on 2021-12-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='cover_letter',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=3, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='has_cv',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_address',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_university_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
