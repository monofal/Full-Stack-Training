from django.db import models


class Jobs(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    entry_timestamp = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(max_length=255, null=True, unique=True)

    class Meta:
        db_table = 'jobs'  # define custom table name
