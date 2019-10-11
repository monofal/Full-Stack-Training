from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from jobs.models import Job, JobApplication


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class HomeView(ListView):
    """
    Home page for jobs
    """
    model = Job
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'
    paginate_by = 6

    def get_queryset(self):
        # get top 20 recently posted jobs
        return self.model.objects.all().order_by("-entry_timestamp")[:20]


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class SearchView(ListView):
    """
    Provide user the ability to search jobs
    """
    model = Job
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        company_name = self.request.GET.get('company_name')
        location = self.request.GET.get('location')
        position = self.request.GET.get('position')
        context['company_name'] = company_name
        context['location'] = location
        context['position'] = position
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            company_name__icontains=self.request.GET['company_name'],
            location__icontains=self.request.GET['location'],
            position__icontains=self.request.GET['position'])\
            .order_by("-entry_timestamp")


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class JobDetailsView(DetailView):
    """
    Get job details by id.
    """
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(JobDetailsView, self).get_context_data(**kwargs)
        context['application'] = JobApplication.objects.filter(job=self.object,
                                                               user=self.request.user).first()
        return context

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
