from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . import models
from portal.models import ReviewProfile
from password_generator import PasswordGenerator
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


class StudentSignUpForm(UserCreationForm):
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

    middle_name = forms.CharField(max_length=20)
    student_university_id = forms.IntegerField()
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    semester = forms.ChoiceField(choices=sem_choices)
    faculty = forms.ChoiceField(choices=fac_choices)
    major = forms.CharField(max_length=20)
    gpa = forms.DecimalField(decimal_places=2, max_digits=3)
    student_address = forms.CharField(max_length=10)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    password1 = None
    password2 = None

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'student_address',
                  'username',
                  'email',
                  'student_university_id',
                  'birthdate',
                  'semester',
                  'faculty',
                  'major',
                  'gpa',)

    @transaction.atomic
    def save(self):
        pwo = PasswordGenerator()
        pw = pwo.generate()

        email_to_send_to = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        message = Mail(
            from_email='iyadelwy2@gmail.com',
            to_emails=email_to_send_to,
            subject='GIU Internship Portal',
            html_content='<h1>Here is your password.</h1>'
                         '<h3>Please change it after logging in</h3>'
                         f'<p>Username: {username} </p>'
                         f'<p>Password: {pw} </p>')
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

        first_n = self.cleaned_data.get('first_name')
        last_n = self.cleaned_data.get('last_name')

        print(pw)
        user = models.User.objects.create(is_student=True, password=pw, first_name=first_n, last_name=last_n,
                                          username=username, email=email_to_send_to)
        user.set_password(pw)
        user.save()
        student = models.Student.objects.create(user=user, middle_name=self.cleaned_data.get('middle_name'),
                                                student_university_id=self.cleaned_data.get('student_university_id'),
                                                birthdate=self.cleaned_data.get('birthdate'),
                                                semester=self.cleaned_data.get('semester'),
                                                faculty=self.cleaned_data.get('faculty'),
                                                major=self.cleaned_data.get('major'),
                                                gpa=self.cleaned_data.get('gpa'),
                                                student_address=self.cleaned_data.get('student_address'),
                                                )

        return user


class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=20)
    employer_address = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    fax_number = forms.CharField(max_length=50, required=False)
    website = forms.CharField(max_length=50)
    type_of_business = forms.CharField(max_length=50)
    establishment_year = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    country_of_origin = forms.CharField(max_length=20)
    industry = forms.CharField(max_length=20)
    number_of_current_employees = forms.IntegerField(required=False)
    products_or_services = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    company_logo = forms.ImageField(max_length=1000, required=False)

    password1 = None
    password2 = None

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username',
                  'email',
                  'company_name',
                  'employer_address',
                  'phone_number',
                  'fax_number',
                  'website',
                  'type_of_business',
                  'establishment_year',
                  'country_of_origin',
                  'industry',
                  'number_of_current_employees',
                  'products_or_services',
                  'company_logo')

    @transaction.atomic
    def save(self):
        pwo = PasswordGenerator()
        pw = pwo.generate()

        email_to_send_to = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        message = Mail(
            from_email='iyadelwy2@gmail.com',
            to_emails=email_to_send_to,
            subject='GIU Internship Portal',
            html_content='<h1>Here is your password.</h1>'
                         '<h3>Please change it after logging in</h3>'
                         f'<p>Username: {username} </p>'
                         f'<p>Password: {pw} </p>')
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

        first_n = "first_name_comp"
        last_n = "last_name_comp"

        # TODO REMOVE
        print(pw)
        user = models.User.objects.create(is_employer=True, password=pw, first_name=first_n, last_name=last_n,
                                          username=username, email=email_to_send_to)
        user.set_password(pw)
        user.save()
        employer = models.Employer.objects.create(user=user,
                                                  company_name=self.cleaned_data.get('company_name'),
                                                  employer_address=self.cleaned_data.get('employer_address'),
                                                  phone_number=self.cleaned_data.get('phone_number'),
                                                  fax_number=self.cleaned_data.get('fax_number'),
                                                  website=self.cleaned_data.get('website'),
                                                  type_of_business=self.cleaned_data.get('type_of_business'),
                                                  establishment_year=self.cleaned_data.get('establishment_year'),
                                                  country_of_origin=self.cleaned_data.get('country_of_origin'),
                                                  industry=self.cleaned_data.get('industry'),
                                                  number_of_current_employees=self.cleaned_data.get(
                                                      'number_of_current_employees'),
                                                  products_or_services=self.cleaned_data.get('products_or_services'),
                                                  company_logo=self.cleaned_data.get('company_logo')
                                                  )
        employer_profile_status = ReviewProfile.objects.create(employer_id=employer)
        employer_profile_status.save()
        contact_person = models.ContactPerson.objects.create(employer_id=employer)
        contact_person.save()
        hr_director = models.HRDirector.objects.create(employer_id=employer)
        hr_director.save()

        return user


class GIUAdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        admin = models.GIUAdmin.objects.create(user=user)

        return user


class FacultyRepresentativeForm(UserCreationForm):
    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    faculty = forms.ChoiceField(choices=fac_choices)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email', 'faculty')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_faculty_representative = True
        user.save()
        fac_rep = models.FacultyRepresentative.objects.create(user=user, faculty=self.cleaned_data.get('faculty'))

        return user


class AcademicAdvisorForm(UserCreationForm):
    fac_choices = (
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Business', 'Business'),
        ('Design', 'Design'),
        ('Architecture', 'Architecture'),
        ('Biotechnology', 'Biotechnology'),
        ('Pharmaceutical', 'Pharmaceutical')

    )

    faculty = forms.ChoiceField(choices=fac_choices)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email', 'faculty')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_academic_advisor = True
        user.save()
        academic_adv = models.AcademicAdvisor.objects.create(user=user, faculty=self.cleaned_data.get('faculty'))
        return user


class CareerOfficeCoordinatorForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_career_office_coordinator = True
        user.save()
        career_o_c = models.CareerOfficeCoordinator.objects.create(user=user)

        return user
