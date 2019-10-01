from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from accounts.forms import EmployeeEditProfile, EmployerEditProfile

from accounts.models import EmployeeProfile, EmployerProfile


class UpdateEmployeeProfileView(UpdateView):
    """
    Update employee/jobseeker profile info
    """
    model = EmployeeProfile
    form_class = EmployeeEditProfile
    context_object_name = 'employee'
    template_name = 'accounts/profile/employee/../../templates/accounts/profile/edit-profile.html'
    success_url = reverse_lazy('accounts:employee-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Record doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = EmployeeProfile.objects.get(user_id=self.request.user.id)
        if obj is None:
            raise Http404("Record doesn't exists")
        return obj


class UpdateEmployerProfileView(UpdateView):
    model = EmployerProfile
    form_class = EmployerEditProfile
    context_object_name = 'employer'
    template_name = 'accounts/profile/employee/../../templates/accounts/profile/edit-profile.html'
    success_url = reverse_lazy('accounts:employer-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Record doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = EmployerProfile.objects.get(user_id=self.request.user.id)
        if obj is None:
            raise Http404("Record doesn't exists")
        return obj
