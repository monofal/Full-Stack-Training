from django.urls import include, path

from jobs.views.employee import ApplyJobView, WithdrawApplication

from .views.employer import ApplicationListView, DashboardView, JobCreateView
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
        path('apply/<int:id>', ApplyJobView.as_view(), name='apply-job'),
        path('withdraw/<int:id>', WithdrawApplication.as_view(), name='withdraw-application'),
    ])),
    path('employer/dashboard',
         DashboardView.as_view(),
         name='employer-dashboard'),
    path('employer/dashboard/applications',
         ApplicationListView.as_view(),
         name='employer-applications'),
    path('employer/job/create',
         JobCreateView.as_view(),
         name='employer-create-job'),
]
