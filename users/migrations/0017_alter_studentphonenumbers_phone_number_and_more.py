# Generated by Django 4.0 on 2021-12-30 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_studentphonenumbers_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentphonenumbers',
            name='phone_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentphonenumbers',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AlterUniqueTogether(
            name='studentphonenumbers',
            unique_together={('student_id', 'phone_number')},
        ),
    ]
