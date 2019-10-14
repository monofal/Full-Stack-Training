from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import *

router = DefaultRouter()
router.register('jobs', JobViewSet, base_name='jobs')

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', SearchApiView.as_view()),
    path('job/<int:id>', GetByJobIdView.as_view()),
    path('employer/applications/', EmployerApplicationsView.as_view()),
    path('employer/jobs/', EmployerJobsView.as_view())
]

urlpatterns += router.urls
