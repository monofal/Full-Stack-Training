import datetime

from django.db import models


# Create your models here.
class Jobs(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    entry_timestamp = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'jobs'  # define custom table name
