import django.utils.timezone
from django.db import models
from users import models as user_models


class ReviewProfile(models.Model):
    job_type_ch = (
        ('In review', 'In review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    employer_id = models.ForeignKey(user_models.Employer, on_delete=models.CASCADE, primary_key=True)
    admin_id = models.ForeignKey(user_models.GIUAdmin, on_delete=models.CASCADE, null=True, blank=True)
    review_status = models.CharField(max_length=20, blank=True, default='In review', choices=job_type_ch)
    reason = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.employer_id.company_name}: {self.review_status}'

    # class Meta:
    #     unique_together = (('employer_id', 'admin_id'),)


class Job(models.Model):
    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    sem_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
    )

    job_type_ch = (
        ('Industrial Internship', 'Industrial Internship'),
        ('Other', 'Other'),
    )

    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    job_description = models.TextField(max_length=1000)
    department = models.CharField(max_length=20)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    application_deadline = models.DateField()
    num_of_available_internships = models.PositiveIntegerField()
    salary_range = models.CharField(max_length=20)
    qualifications = models.TextField(max_length=500)
    job_location = models.CharField(max_length=20)
    application_link = models.CharField(max_length=50, null=True, blank=True)
    application_email = models.CharField(max_length=50, null=True, blank=True)
    job_type = models.CharField(max_length=30, choices=job_type_ch)
    employer_id = models.ForeignKey(user_models.Employer, on_delete=models.CASCADE)
    allowed_faculties = models.TextField(max_length=300, choices=fac_choices)
    required_semesters = models.IntegerField(max_length=20, choices=sem_choices)
    # for later elegibility
    aa_id = models.ForeignKey(user_models.AcademicAdvisor, null=True, blank=True, on_delete=models.DO_NOTHING)
    visibility_fac_rep = models.BooleanField(default=False, blank=True)
    visibility_admin = models.BooleanField(default=False, blank=True, verbose_name='Visibility')

    active_student = models.OneToOneField(user_models.Student, null=True, blank=True, on_delete=models.DO_NOTHING)
    post_is_up = models.BooleanField(default=True, verbose_name='Visible')

    def __str__(self):
        return self.title

    @property
    def duration(self):
        return self.job_end_date.month - self.job_start_date.month


class Application(models.Model):
    job_type_ch = (
        ('In review', 'In review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    application_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(user_models.Student, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=20, default='In review', blank=True, choices=job_type_ch)
    visibility_for_employer = models.BooleanField(default=False, blank=True)
    application_date = models.DateField(default=django.utils.timezone.now, blank=True)
    has_ended = models.BooleanField(default=False, blank=True)
    has_started = models.BooleanField(default=False, blank=True)
    confirm = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.job_id.title}'

    class Meta:
        unique_together = (('student_id', 'job_id'),)


class ProgressReport(models.Model):
    progress_report_id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, verbose_name='Job')
    student_id = models.ForeignKey(user_models.Student, on_delete=models.CASCADE)
    academic_advisor_id = models.ForeignKey(user_models.AcademicAdvisor, on_delete=models.CASCADE, null=True)
    progress_report_title = models.CharField(max_length=100, blank=True)
    progress_report_date = models.DateField(default=django.utils.timezone.now, blank=True)
    numeric_state = models.PositiveIntegerField(default=0, blank=True)
    evaluation = models.TextField(max_length=300, default='', blank=True)
    progress_report_description = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return f'{self.student_id.user.username} '
