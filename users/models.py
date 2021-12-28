from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Parent User
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_faculty_representative = models.BooleanField(default=False)
    is_academic_advisor = models.BooleanField(default=False)
    is_career_office_coordinator = models.BooleanField(default=False)


# All users
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    student_university_id = models.PositiveIntegerField()
    birthdate = models.DateField()
    semester = models.IntegerField()
    faculty = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    gpa = models.DecimalField(decimal_places=2, max_digits=3)
    student_address = models.CharField(max_length=10)
    has_cv = models.BooleanField(default=False, blank=True)
    cover_letter = models.TextField(max_length=1000, default='', blank=True)

    @property
    def age(self):
        return self.birthdate.year - datetime.now().year

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=20)
    employer_address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=50, null=True, blank=True)
    website = models.CharField(max_length=50)
    type_of_business = models.CharField(max_length=50)
    establishment_year = models.DateField()
    country_of_origin = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    number_of_current_employees = models.PositiveIntegerField(null=True, blank=True)
    products_or_services = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name


class GIUAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class FacultyRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class AcademicAdvisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class CareerOfficeCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


# other tables

class StudentPhoneNumbers(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number

    class Meta:
        unique_together = (('student_id', 'phone_number'),)


class ContactPerson(models.Model):
    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    contact_person_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    fax = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.contact_person_name


class HRDirector(models.Model):
    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    hr_name = models.CharField(max_length=20)
    hr_email = models.CharField(max_length=50)

    def __str__(self):
        return self.hr_name


class ReviewProfile(models.Model):
    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    admin_id = models.OneToOneField(GIUAdmin, on_delete=models.CASCADE)
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
    employer_id = models.OneToOneField(Employer, on_delete=models.DO_NOTHING)
    admin_id = models.OneToOneField(GIUAdmin, on_delete=models.DO_NOTHING)
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
    aa_id = models.OneToOneField(AcademicAdvisor, on_delete=models.DO_NOTHING)
    faculty_rep = models.OneToOneField(FacultyRepresentative, on_delete=models.DO_NOTHING)


class CvBuilder(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.DO_NOTHING)
    personal_phone = models.CharField(max_length=30)
    personal_email = models.CharField(max_length=50)
    education = models.TextField(max_length=100)
    extracurricular_activities = models.TextField(max_length=300)
    skills = models.TextField(max_length=300)
    achievements = models.TextField(max_length=300)
    languages = models.TextField(max_length=100)
    interests = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    linked_in_link = models.CharField(max_length=30)
    github_link = models.CharField(max_length=30)

    def __str__(self):
        return f"CV: {self.student_id.first_name} {self.student_id.last_name}"


class Application(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.DO_NOTHING, primary_key=True)
    job_id = models.OneToOneField(Job, on_delete=models.DO_NOTHING)
    application_status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student_id.user.username} applies to {self.job_id.title}'

    class Meta:
        unique_together = (('student_id', 'job_id'),)


class Eligible(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.DO_NOTHING, primary_key=True)
    II_id = models.OneToOneField(IndustrialInternship, on_delete=models.DO_NOTHING)
    coc_id = models.OneToOneField(CareerOfficeCoordinator, on_delete=models.DO_NOTHING)
    eligibility = models.BooleanField()

    def __str__(self):
        return f'{self.student_id.user.username} eligible: {self.eligibility}'

    class Meta:
        unique_together = (('student_id', 'II_id'),)


class ProgressReport(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.DO_NOTHING, primary_key=True)
    academic_advisor_id = models.OneToOneField(AcademicAdvisor, on_delete=models.DO_NOTHING)
    progress_report_date = models.DateField()
    numeric_state = models.PositiveIntegerField()
    evaluation = models.TextField(max_length=300)
    progress_report_description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_id.user.username} report'

    class Meta:
        unique_together = (('student_id', 'academic_advisor_id'),)
