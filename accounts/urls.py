from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views.account import RegisterView, LogoutView, LoginView, activate
from accounts.views.profile import UpdateEmployeeProfileView, UpdateEmployerProfileView

app_name = "accounts"

urlpatterns = [
    path('register',
         RegisterView.as_view(),
         name='register'),
    path('logout',
         LogoutView.as_view(),
         name='logout'),
    path('login',
         LoginView.as_view(),
         name='login'),
    path('accounts/employee/update',
         UpdateEmployeeProfileView.as_view(),
         name='employee-profile-update'),
    path('accounts/employer/update',
         UpdateEmployerProfileView.as_view(),
         name='employer-profile-update'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate,
            name='activate'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
