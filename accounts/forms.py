"""
Account forms
"""
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from accounts.models import EmployeeProfile, EmployerProfile
from django.contrib.auth import get_user_model

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
        error_messages = {
            'role': {
                'required': 'Role is required'
            }
        }

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

    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'years_of_experience', 'profile_image', 'gender']


class EmployerEditProfile(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super(EmployerEditProfile, self).__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'First name'
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