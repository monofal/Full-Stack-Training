from rest_framework import viewsets

from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SearchApiView(ListAPIView):
    """
    Return list of jobs that matches search parameters
    """
    serializer_class = JobSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(
            company_name__icontains=self.request.query_params.get('company_name', ''),
            location__icontains=self.request.query_params.get('location', ''),
            position__icontains=self.request.query_params.get('position', '')).order_by("-entry_timestamp")


class GetByJobIdView(ListAPIView):
    """
    Provide job by job id
    """
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        job_id = self.kwargs['id']
        if job_id:
            return self.serializer_class.Meta.model.objects.filter(id=job_id)
        return queryset


class EmployerApplicationsView(ListAPIView):
    """
    List of applications applied against jobs posted by specific user
    """
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        employer_id = self.request.query_params.get('employer_id')
        if employer_id:
            return self.serializer_class.Meta.model.objects.filter(job__user_id=employer_id). \
                order_by('-applied_timestamp')


class EmployerJobsView(ListAPIView):
    """
    Provider list of jobs posted by employer
    """
    serializer_class = JobSerializer

    def get_queryset(self):
        employer_id = self.request.query_params.get('employer_id')
        if employer_id:
            return self.serializer_class.Meta.model.objects.filter(user_id=employer_id). \
                order_by('-entry_timestamp')
