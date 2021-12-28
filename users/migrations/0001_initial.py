# Generated by Django 4.0 on 2021-12-27 17:03

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_faculty_representative', models.BooleanField(default=False)),
                ('is_academic_advisor', models.BooleanField(default=False)),
                ('is_career_office_coordinator', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AcademicAdvisor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('faculty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CareerOfficeCoordinator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('company_name', models.CharField(max_length=20)),
                ('employer_address', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(max_length=50)),
                ('type_of_business', models.CharField(max_length=50)),
                ('establishment_year', models.DateField()),
                ('country_of_origin', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=20)),
                ('number_of_current_employees', models.PositiveIntegerField()),
                ('products_or_services', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyRepresentative',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('faculty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GIUAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_university_id', models.PositiveIntegerField()),
                ('birthdate', models.DateField()),
                ('semester', models.IntegerField()),
                ('faculty', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=3)),
                ('student_address', models.CharField(max_length=10)),
                ('has_cv', models.BooleanField(blank=True, default=False)),
                ('cover_letter', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('contact_person_name', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=20)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HRDirector',
            fields=[
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('hr_name', models.CharField(max_length=20)),
                ('hr_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('job_description', models.TextField(max_length=50)),
                ('department', models.CharField(max_length=20)),
                ('job_start_date', models.DateField()),
                ('job_end_date', models.DateField()),
                ('application_deadline', models.DateField()),
                ('num_of_available_internships', models.PositiveIntegerField()),
                ('salary_range', models.CharField(max_length=20)),
                ('qualifications', models.TextField(max_length=100)),
                ('job_location', models.CharField(max_length=20)),
                ('application_link', models.CharField(max_length=50)),
                ('application_email', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=30)),
                ('visibility', models.BooleanField(blank=True, default=False)),
                ('reason', models.TextField(max_length=100)),
                ('allowed_faculties', models.TextField(max_length=300)),
                ('required_semesters', models.CharField(max_length=20)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.giuadmin')),
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.employer')),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialInternship',
            fields=[
                ('industrial_internship_ID', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.job')),
                ('industrial_Internship_status', models.CharField(max_length=20)),
                ('aa_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.academicadvisor')),
                ('faculty_rep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.facultyrepresentative')),
            ],
        ),
        migrations.CreateModel(
            name='CvBuilder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_phone', models.CharField(max_length=30)),
                ('personal_email', models.CharField(max_length=50)),
                ('education', models.TextField(max_length=100)),
                ('extracurricular_activities', models.TextField(max_length=300)),
                ('skills', models.TextField(max_length=300)),
                ('achievements', models.TextField(max_length=300)),
                ('languages', models.TextField(max_length=100)),
                ('interests', models.TextField(max_length=100)),
                ('experience', models.TextField(max_length=100)),
                ('linked_in_link', models.CharField(max_length=30)),
                ('github_link', models.CharField(max_length=30)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPhoneNumbers',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.student')),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('student_id', 'phone_number')},
            },
        ),
        migrations.CreateModel(
            name='ReviewProfile',
            fields=[
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('review_status', models.CharField(max_length=20)),
                ('reason', models.TextField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.giuadmin')),
            ],
            options={
                'unique_together': {('employer_id', 'admin_id')},
            },
        ),
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student')),
                ('progress_report_date', models.DateField()),
                ('numeric_state', models.PositiveIntegerField()),
                ('evaluation', models.TextField(max_length=300)),
                ('progress_report_description', models.CharField(max_length=100)),
                ('academic_advisor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.academicadvisor')),
            ],
            options={
                'unique_together': {('student_id', 'academic_advisor_id')},
            },
        ),
        migrations.CreateModel(
            name='Eligable',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student')),
                ('eligibility', models.BooleanField()),
                ('II_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.industrialinternship')),
                ('coc_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.careerofficecoordinator')),
            ],
            options={
                'unique_together': {('student_id', 'II_id')},
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.student')),
                ('application_status', models.CharField(max_length=20)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.job')),
            ],
            options={
                'unique_together': {('student_id', 'job_id')},
            },
        ),
    ]