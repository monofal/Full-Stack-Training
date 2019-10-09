from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalDeleteView,
                                           BSModalUpdateView)
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from jobs.decorators import is_employee
from jobs.forms import ApplyJobForm
from jobs.models import JobApplication


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class ApplyJobView(BSModalCreateView):
    """
    Provide employee ability to apply for a job
    """
    template_name = 'jobs/employee/apply_job.html'
    form_class = ApplyJobForm
    success_message = 'You have successfully applied for this job'
    success_url = reverse_lazy('jobs:home')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class UpdateApplicationView(BSModalUpdateView):
    """
    Provide employee ability to update job application
    """
    model = JobApplication
    template_name = 'jobs/employee/update_application.html'
    form_class = ApplyJobForm
    success_message = 'Success: Application terms updated.'
    success_url = reverse_lazy('jobs:home')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class DeleteApplicationView(BSModalDeleteView):
    """
    Provide employee ability to withdraw job application
    """
    model = JobApplication
    template_name = 'jobs/employee/withdraw_application.html'
    success_message = 'Success: Application withdrawn.'
    success_url = reverse_lazy('jobs:home')
