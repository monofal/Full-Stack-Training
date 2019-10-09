from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from accounts.views.account import (LoginView, LogoutView, RegisterView,
                                    activate)
from accounts.views.profile import (AddDocumentView, AddQualificationView,
                                    DeleteDocumentView,
                                    DeleteQualificationView,
                                    UpdateDocumentView,
                                    UpdateEmployeeProfileView,
                                    UpdateEmployerProfileView,
                                    UpdateQualificationView)

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
    path('employee/qualification/', include([
         path('add', AddQualificationView.as_view(), name='add-qualification'),
         path('update/<int:pk>', UpdateQualificationView.as_view(), name='update-qualification'),
         path('delete/<int:pk>', DeleteQualificationView.as_view(), name='delete-qualification'),
    ])),
    path('employee/document/', include([
         path('add', AddDocumentView.as_view(), name='add-document'),
         path('update/<int:pk>', UpdateDocumentView.as_view(), name='update-document'),
         path('delete/<int:pk>', DeleteDocumentView.as_view(), name='delete-document'),
    ])),
    path('accounts/employer/update',
         UpdateEmployerProfileView.as_view(),
         name='employer-profile-update'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate,
            name='activate'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
