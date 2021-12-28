# Generated by Django 4.0 on 2021-12-27 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_student_middle_name_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='employer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer'),
        ),
        migrations.AlterField(
            model_name='cvbuilder',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student'),
        ),
        migrations.AlterField(
            model_name='eligible',
            name='II_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.industrialinternship'),
        ),
        migrations.AlterField(
            model_name='eligible',
            name='coc_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.careerofficecoordinator'),
        ),
        migrations.AlterField(
            model_name='eligible',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student'),
        ),
        migrations.AlterField(
            model_name='hrdirector',
            name='employer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer'),
        ),
        migrations.AlterField(
            model_name='industrialinternship',
            name='aa_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.academicadvisor'),
        ),
        migrations.AlterField(
            model_name='industrialinternship',
            name='faculty_rep',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.facultyrepresentative'),
        ),
        migrations.AlterField(
            model_name='job',
            name='admin_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.giuadmin'),
        ),
        migrations.AlterField(
            model_name='job',
            name='employer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.employer'),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='academic_advisor_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.academicadvisor'),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student'),
        ),
        migrations.AlterField(
            model_name='reviewprofile',
            name='admin_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.giuadmin'),
        ),
        migrations.AlterField(
            model_name='reviewprofile',
            name='employer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user'),
        ),
        migrations.AlterField(
            model_name='studentphonenumbers',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.student'),
        ),
    ]