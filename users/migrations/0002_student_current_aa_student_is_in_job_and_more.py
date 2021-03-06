# Generated by Django 4.0 on 2022-01-06 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_aa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.academicadvisor'),
        ),
        migrations.AddField(
            model_name='student',
            name='is_in_job',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='academicadvisor',
            name='faculty',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Computer Science', 'Computer Science'), ('Business', 'Business'), ('Design', 'Design'), ('Architecture', 'Architecture'), ('Biotechnology', 'Biotechnology'), ('Pharmaceutical', 'Pharmaceutical')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='facultyrepresentative',
            name='faculty',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Computer Science', 'Computer Science'), ('Business', 'Business'), ('Design', 'Design'), ('Architecture', 'Architecture'), ('Biotechnology', 'Biotechnology'), ('Pharmaceutical', 'Pharmaceutical')], max_length=20),
        ),
    ]
