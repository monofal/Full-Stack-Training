"""
Account models
"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    User manager class
    """

    def create_superuser(
            self, email, password,
            is_active=True, is_staff=True, is_superuser=True, **extra_fields
    ):
        """
        Create a super user
        """
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """
    role = models.CharField(
        max_length=12,
        default='',
        error_messages={
          'required': "Role must be provided"
        })
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            'unique': "A user with that email already exists.",
        })
    is_email_confirmed = models.BooleanField(default=False, blank=False)
    is_active = models.BooleanField(default=True, blank=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()


class Skill(models.Model):
    """
    Lookup table for employee skills
    """
    name = models.CharField(
        blank=True,
        max_length=100
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    """
    Employee profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    first_name = models.CharField(
        blank=True,
        null=True,
        default='',
        max_length=50
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        default='',
        max_length=50
    )
    years_of_experience = models.FloatField(
        blank=True,
        null=True,
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


class EmployerProfile(models.Model):
    """
    Employer/Company profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(
        blank=True,
        null=True,
        default='',
        max_length=50
    )
    address = models.CharField(
        blank=True,
        null=True,
        default='',
        max_length=255
    )
    updated_at = models.DateTimeField(default=timezone.now)


class Document(models.Model):
    """
    Document model
    """
    employee_profile = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    document_file = models.FileField(
        blank=True,
        null=True
    )


class Qualification(models.Model):
    """
    Hold employee qualification information
    """
    employee_profile = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE
    )
    institute = models.CharField(
        max_length=255,
        error_messages={
            'required': "Institute name must be provided"
        })
    degree = models.CharField(
        max_length=255,
        error_messages={
            'required': "Degree must be provided"
        })
    start_date = models.DateField()
    end_date = models.DateField()
    percentage_marks = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    cgpa = models.FloatField(
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(4.00)]
    )

    def __str__(self):
        return self.degree


def create_profile(sender, **kwargs):
    """
    Create a profile record each time a new user is registered
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        if user.role == 'employee':
            user_profile = EmployeeProfile(user=user)
        else:
            user_profile = EmployerProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
