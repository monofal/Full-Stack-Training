"""
Account models
"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.utils import timezone


class User(AbstractBaseUser):
    """
    User model
    """
    role = models.CharField(max_length=12,
                            default='employee',
                            error_messages={
                                'required': "Role must be provided"
                            })
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    is_email_confirmed = models.BooleanField(default=False, blank=False)
    is_active = models.BooleanField(default=True, blank=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        db_table = 'user'  # define custom table name


class EmployeeProfile(models.Model):
    """
    Employee profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    years_of_experience = models.FloatField(
        blank=True,
        default=0.00
    )
    profile_image = models.ImageField(
        upload_to='img',
        blank=True
    )
    gender = models.CharField(
        blank=True,
        null=True,
        default='',
        max_length=10
    )
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'employee_profile'  # define custom table name


class EmployerProfile(models.Model):
    """
    Employer/Company profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    address = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'employer_profile'  # define custom table name


def create_profile(sender, **kwargs):
    """
    Create a profile record each time a new user is registered
    :param sender:
    :param kwargs:
    :return:
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        if user.role == 'employee':
            user_profile = EmployeeProfile(user=user)
        else:
            user_profile = EmployerProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
