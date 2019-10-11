from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from jobs.decorators import is_employer
from jobs.forms import CreateJobForm
from jobs.models import Job, JobApplication


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employer, name='dispatch')
class DashboardView(SuccessMessageMixin, ListView):
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by('-entry_timestamp')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employer, name='dispatch')
class ApplicationListView(ListView):
    model = JobApplication
    template_name = 'jobs/employer/applications.html'
    context_object_name = 'applications'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(job__user_id=self.request.user.id).order_by('-applied_timestamp')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employer, name='dispatch')
class JobCreateView(SuccessMessageMixin, CreateView):
    """
    Provide employer ability to create a new job
    """
    template_name = 'jobs/employer/create_job.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_message = 'Success: Job published successfully.'
    success_url = reverse_lazy('jobs:home')

    def dispatch(self, request, *args, **kwargs):
        """
        Show error message if user hasn't confirmed his email
        """
        if not self.request.user.is_email_confirmed:
            messages.error(self.request, 'Error: Please confirm your email to publish a job.')
            return HttpResponseRedirect(reverse_lazy('jobs:employer-dashboard'))
        else:
            return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
