"""
Account models
"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import UserManager


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
