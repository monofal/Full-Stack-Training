from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from jobs.decorators import is_employee
from jobs.forms import ApplyJobForm
from jobs.models import JobApplication


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class ApplyJobView(CreateView):
    model = JobApplication
    form_class = ApplyJobForm

    def dispatch(self, request, *args, **kwargs):
        """
        Show error message if user hasn't confirmed his email
        """
        if not self.request.user.is_email_confirmed:
            messages.error(self.request, 'Error: Please confirm your email to apply for this job')
            return HttpResponseRedirect(reverse_lazy('jobs:job-detail', kwargs={'id': self.kwargs['id']}))
        else:
            return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Success: Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('jobs:home'))

    def get_success_url(self):
        return reverse_lazy('jobs:job-detail', kwargs={'id': self.kwargs['id']})

    def form_valid(self, form):
        # save applicant
        form.instance.user = self.request.user
        form.instance.job_id = self.request.POST.get('job_id', None)
        form.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class WithdrawApplication(DeleteView):
    """
    Provide employee ability to withdraw job application
    """
    model = JobApplication
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get_success_url(self):
        messages.info(self.request, 'Success : Application successfully withdrawn')
        return reverse_lazy('jobs:job-detail', kwargs={'id': self.request.POST.get('job_id', None)})

    def form_valid(self, form):
        # save applicant
        form.instance.job_id = self.request.POST.get('job_id', None)
        form.save()
        return super().form_valid(form)
