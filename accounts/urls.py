from django.urls import path, re_path
from accounts.views import RegisterEmployeeView, LoginView, LogoutView, activate

app_name = "accounts"

urlpatterns = [
    path('employee/register',
         RegisterEmployeeView.as_view(),
         name='employee-register'),
    path('logout',
         LogoutView.as_view(),
         name='logout'),
    path('login',
         LoginView.as_view(),
         name='login'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate,
            name='activate'),
]
