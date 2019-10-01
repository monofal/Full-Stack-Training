from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Jobs


class HomeView(ListView):
    """
    Home page for jobs
    """
    model = Jobs
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'
    paginate_by = 6

    def get_queryset(self):
        # get top 20 recently posted jobs
        return self.model.objects.all().order_by("-entry_timestamp")[:20]


class SearchView(ListView):
    """
    Provide user the ability to search jobs
    """
    model = Jobs
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
        return self.model.objects.filter(company_name__icontains=self.request.GET['company_name'],
                                         location__icontains=self.request.GET['location'],
                                         position__icontains=self.request.GET['position']).order_by("-entry_timestamp")


class JobDetailsView(DetailView):
    """
    Get job details by id.
    """
    model = Jobs
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

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
