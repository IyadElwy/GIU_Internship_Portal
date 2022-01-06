from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.urls import reverse_lazy
from django.conf import settings

# Parent User
import users


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_faculty_representative = models.BooleanField(default=False)
    is_academic_advisor = models.BooleanField(default=False)
    is_career_office_coordinator = models.BooleanField(default=False)
    password = models.CharField(null=True, blank=True, max_length=500)


# All users


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=20)
    employer_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=50, null=True, blank=True)
    website = models.CharField(max_length=50)
    type_of_business = models.CharField(max_length=50)
    establishment_year = models.DateField()
    country_of_origin = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    number_of_current_employees = models.PositiveIntegerField(null=True, blank=True)
    products_or_services = models.CharField(max_length=30)
    company_logo = models.ImageField(upload_to=str(settings.MEDIA_ROOT) + '/company_images/', blank=True, null=True,
                                     default='company_images/default.png', max_length=1000)

    def __str__(self):
        return self.company_name


class GIUAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class FacultyRepresentative(models.Model):
    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty = models.CharField(max_length=20, choices=fac_choices)

    def __str__(self):
        return self.faculty


class AcademicAdvisor(models.Model):
    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty = models.CharField(max_length=20, choices=fac_choices)

    def __str__(self):
        return self.user.username


class Student(models.Model):
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

    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    middle_name = models.CharField(max_length=20)
    student_university_id = models.PositiveIntegerField()
    birthdate = models.DateField()
    semester = models.IntegerField(choices=sem_choices)
    faculty = models.CharField(max_length=20, choices=fac_choices)
    major = models.CharField(max_length=20)
    gpa = models.DecimalField(decimal_places=2, max_digits=3)
    student_address = models.CharField(max_length=10)
    has_cv = models.BooleanField(default=False, blank=True)
    cover_letter = models.TextField(max_length=1000, default='', blank=True)
    is_in_job = models.BooleanField(default=False)
    current_aa = models.ForeignKey(AcademicAdvisor, on_delete=models.DO_NOTHING, null=True, blank=True)

    @property
    def age(self):
        return datetime.now().year - self.birthdate.year

    def __str__(self):
        return self.user.username


class CareerOfficeCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


# other tables


class StudentPhoneNumbers(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        unique_together = (('student_id', 'phone_number'),)


class ContactPerson(models.Model):
    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    contact_person_name = models.CharField(max_length=20, blank=True, null=True, default='None')
    job_title = models.CharField(max_length=30, blank=True, null=True, default='None')
    email = models.CharField(max_length=50, blank=True, null=True, default='None')
    mobile_number = models.CharField(max_length=20, blank=True, null=True, default='None')
    fax = models.CharField(max_length=50, null=True, blank=True, default='None')

    def __str__(self):
        return self.contact_person_name


class HRDirector(models.Model):
    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    hr_name = models.CharField(max_length=20, blank=True, null=True, default='None')
    hr_email = models.CharField(max_length=50, blank=True, null=True, default='None')

    def __str__(self):
        return self.hr_name
