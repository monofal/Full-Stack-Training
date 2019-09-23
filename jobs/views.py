from django.http import HttpResponse
from django.shortcuts import render

from .models import Jobs


# Create your views here.
def job_view(request, *args, **kwargs):
    # get 20 records from database
    jobs = Jobs.objects.all()[:20]
    context = {
        'jobs': jobs
    }
    return render(request, 'job/jobs.html', context)
