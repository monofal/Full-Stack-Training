from rest_framework import serializers

from ..models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('company_name', 'position', 'location', 'description', 'category', 'type', 'last_date',)


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"
