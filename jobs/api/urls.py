from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('jobs', JobViewSet, base_name='jobs')

urlpatterns = [
    path('search/', SearchApiView.as_view()),
    path('job/<int:id>', GetByJobIdView.as_view()),
    path('employer/applications/', EmployerApplicationsView.as_view()),
    path('employer/jobs/', EmployerJobsView.as_view())
]

urlpatterns += router.urls
