from django.urls import include, path

from jobs.views.employee import (ApplyJobView, DeleteApplicationView,
                                 UpdateApplicationView)

from .views.employer import JobCreateView
from .views.home import HomeView, JobDetailsView, SearchView

app_name = "jobs"

urlpatterns = [
    path('',
         HomeView.as_view(),
         name='home'),
    path('search',
         SearchView.as_view(),
         name='search'),
    path('job/<int:id>',
         JobDetailsView.as_view(),
         name='job-detail'),
    path('employee/job/application/', include([
        path('apply', ApplyJobView.as_view(), name='apply-job'),
        path('update/<int:pk>', UpdateApplicationView.as_view(), name='update-application'),
        path('delete/<int:pk>', DeleteApplicationView.as_view(), name='delete-application'),
    ])),
    path('employer/job/create',
         JobCreateView.as_view(),
         name='employer-create-job'),
]
