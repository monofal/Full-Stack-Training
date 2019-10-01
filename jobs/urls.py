from django.urls import path
from jobs.views import HomeView, SearchView, JobDetailsView

app_name = "jobs"

urlpatterns = [
    path('',
         HomeView.as_view(),
         name='home'),
    path('search',
         SearchView.as_view(),
         name='search'),
    path('jobs/<int:id>',
         JobDetailsView.as_view(),
         name='jobs-detail'),
]
