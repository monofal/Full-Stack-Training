from django.db import models
from django.utils import timezone

from accounts.forms import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    """
    Job model
    """
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    company_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField()
    type = models.CharField(
        choices=JOB_TYPE,
        max_length=12
    )
    category = models.CharField(max_length=50)
    last_date = models.DateTimeField()
    entry_timestamp = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(
        max_length=255,
        null=True,
        unique=True
    )
    is_active = models.BooleanField(
        default=True,
        blank=False
    )


class JobApplication(models.Model):
    """
    Job application model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    applied_timestamp = models.DateTimeField(default=timezone.now)
    cover_letter = models.TextField()
