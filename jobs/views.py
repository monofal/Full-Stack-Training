from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Jobs


@login_required(login_url='/login')
def home_view(request, *args, **kwargs):
    # get latest 20 records from database
    jobs = Jobs.objects.all().order_by("-entry_timestamp")[:20]
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)
