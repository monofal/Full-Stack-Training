"""
Account forms
"""
from bootstrap_modal_forms.forms import BSModalForm
from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_select2.forms import Select2MultipleWidget

from accounts.models import (Document, EmployeeProfile, EmployerProfile,
                             Qualification)

User = get_user_model()

ROLE_CHOICES = (
    ('employee', 'Employee'),
    ('employer', 'Employer'))


class RegistrationForm(UserCreationForm):
    """
    Employee/JobSeeker registration form
    """

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'role']

    def save(self,
             commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    User login form
    """
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class EmployeeEditProfile(forms.ModelForm):
    """
    Employee edit profile form
    """
    def __int__(self, *args, **kwargs):
        super(EmployeeEditProfile, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'First name'
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Last name'
            }
        )
        self.fields['years_of_experience'].widget.attrs.update(
            {
                'placeholder': 'Years of exp'
            }
        )
        self.fields['profile_image'].widget.attrs.update(
            {
                'placeholder': 'Upload new profile image'
            }
        )

    class Meta:
        model = EmployeeProfile
        widgets = {
            'skills': Select2MultipleWidget
        }
        fields = ['profile_image', 'first_name', 'last_name', 'years_of_experience', 'gender', 'skills']


class EmployerEditProfile(forms.ModelForm):
    """
    Employee edit profile form
    """
    def __int__(self, *args, **kwargs):
        super(EmployerEditProfile, self).__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company name'
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address'
            }
        )

    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'address']


class QualificationForm(BSModalForm):
    """
    Employee qualification/degree form
    """
    class Meta:
        model = Qualification
        widgets = {
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'percentage_marks': forms.TextInput(attrs={'class': 'form-control'}),
            'cgpa': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = ['institute', 'degree', 'start_date', 'end_date', 'percentage_marks', 'cgpa']

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date < start_date:
            msg = u"End date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])

    def save(self, commit=False):

        if not self.request.is_ajax():
            qualification = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            qualification.employee_profile_id = EmployeeProfile.objects.get(user_id=self.request.user.pk).id
            qualification.save()
        else:
            qualification = super(CreateUpdateAjaxMixin, self).save(commit=False)

        return qualification


class DocumentForm(BSModalForm):
    """
    Employee document form
    """
    class Meta:
        model = Document
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        fields = ['name', 'description', 'document_file']

    def save(self, commit=False):

        if self.request.is_ajax():
            document = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            document.employee_profile_id = EmployeeProfile.objects.get(user_id=self.request.user.pk).id
            document.save()
        else:
            document = super(CreateUpdateAjaxMixin, self).save(commit=False)

        return document
