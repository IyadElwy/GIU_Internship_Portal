from django.db import models
from users import models as user_models


class ReviewProfile(models.Model):
    employer_id = models.OneToOneField(user_models.Employer, on_delete=models.CASCADE, primary_key=True)
    admin_id = models.OneToOneField(user_models.GIUAdmin, on_delete=models.CASCADE)
    review_status = models.CharField(max_length=20)
    reason = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.employer_id.company_name}: {self.review_status}'

    class Meta:
        unique_together = (('employer_id', 'admin_id'),)


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    job_description = models.TextField(max_length=50)
    department = models.CharField(max_length=20)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    application_deadline = models.DateField()
    num_of_available_internships = models.PositiveIntegerField()
    salary_range = models.CharField(max_length=20)
    qualifications = models.TextField(max_length=100)
    job_location = models.CharField(max_length=20)
    application_link = models.CharField(max_length=50)
    application_email = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30)
    employer_id = models.OneToOneField(user_models.Employer, on_delete=models.DO_NOTHING)
    admin_id = models.OneToOneField(user_models.GIUAdmin, on_delete=models.DO_NOTHING)
    visibility = models.BooleanField(default=False, blank=True)
    reason = models.TextField(max_length=100)
    allowed_faculties = models.TextField(max_length=300)
    required_semesters = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    @property
    def duration(self):
        return self.job_end_date.month - self.job_start_date.month


class IndustrialInternship(models.Model):
    industrial_internship_ID = models.OneToOneField(Job, primary_key=True, on_delete=models.DO_NOTHING)
    industrial_Internship_status = models.CharField(max_length=20)
    aa_id = models.OneToOneField(user_models.AcademicAdvisor, on_delete=models.DO_NOTHING)
    faculty_rep = models.OneToOneField(user_models.FacultyRepresentative, on_delete=models.DO_NOTHING)


class Application(models.Model):
    student_id = models.OneToOneField(user_models.Student, on_delete=models.DO_NOTHING, primary_key=True)
    job_id = models.OneToOneField(Job, on_delete=models.DO_NOTHING)
    application_status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student_id.user.username} applies to {self.job_id.title}'

    class Meta:
        unique_together = (('student_id', 'job_id'),)


class Eligible(models.Model):
    student_id = models.OneToOneField(user_models.Student, on_delete=models.DO_NOTHING, primary_key=True)
    II_id = models.OneToOneField(IndustrialInternship, on_delete=models.DO_NOTHING)
    coc_id = models.OneToOneField(user_models.CareerOfficeCoordinator, on_delete=models.DO_NOTHING)
    eligibility = models.BooleanField()

    def __str__(self):
        return f'{self.student_id.user.username} eligible: {self.eligibility}'

    class Meta:
        unique_together = (('student_id', 'II_id'),)


class ProgressReport(models.Model):
    student_id = models.OneToOneField(user_models.Student, on_delete=models.DO_NOTHING, primary_key=True)
    academic_advisor_id = models.OneToOneField(user_models.AcademicAdvisor, on_delete=models.DO_NOTHING)
    progress_report_date = models.DateField()
    numeric_state = models.PositiveIntegerField()
    evaluation = models.TextField(max_length=300)
    progress_report_description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_id.user.username} report'

    class Meta:
        unique_together = (('student_id', 'academic_advisor_id'),)