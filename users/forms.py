from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . import models


class StudentSignUpForm(UserCreationForm):
    middle_name = forms.CharField(max_length=20)
    student_university_id = forms.IntegerField()
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    semester = forms.IntegerField()
    faculty = forms.CharField(max_length=20)
    major = forms.CharField(max_length=20)
    gpa = forms.DecimalField(decimal_places=2, max_digits=3)
    student_address = forms.CharField(max_length=10)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'student_address',
                  'username',
                  'email',
                  'password1',
                  'password2',
                  'student_university_id',
                  'birthdate',
                  'semester',
                  'faculty',
                  'major',
                  'gpa',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
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

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
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
                  'products_or_services')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
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
                                                  products_or_services=self.cleaned_data.get('products_or_services')
                                                  )

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
        user.save()
        admin = models.GIUAdmin.objects.create(user=user)

        return user


class FacultyRepresentativeForm(UserCreationForm):
    faculty = forms.CharField(max_length=20)
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
    faculty = forms.CharField(max_length=20)
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
