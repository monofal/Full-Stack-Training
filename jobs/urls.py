from django.urls import path
from jobs.views import home_view

app_name = "jobs"

urlpatterns = [
    path('home',
         home_view),
]
