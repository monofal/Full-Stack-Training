from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalDeleteView,
                                           BSModalUpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from accounts.forms import (DocumentForm, EmployeeEditProfile,
                            EmployerEditProfile, QualificationForm)
from accounts.models import (Document, EmployeeProfile, EmployerProfile,
                             Qualification)
from jobs.decorators import is_employee, is_employer


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class UpdateEmployeeProfileView(SuccessMessageMixin, UpdateView):
    """
    Update employee/jobseeker profile info
    """
    model = EmployeeProfile
    form_class = EmployeeEditProfile
    context_object_name = 'employee'
    template_name = 'accounts/profile/edit_profile.html'
    success_message = 'Success: Profile information updated.'
    success_url = reverse_lazy('accounts:employee-profile-update')

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployeeProfileView, self).get_context_data(**kwargs)
        context['qualifications'] = Qualification.objects.filter(employee_profile=self.object)
        context['documents'] = Document.objects.filter(employee_profile=self.object)
        return context

    def get_object(self, queryset=None):
        obj = EmployeeProfile.objects.get(user_id=self.request.user.id)
        if obj is None:
            raise Http404("Record doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Record doesn't exists")
        return self.render_to_response(self.get_context_data())


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employer, name='dispatch')
class UpdateEmployerProfileView(SuccessMessageMixin, UpdateView):
    """
    Update employer/company profile info
    """
    model = EmployerProfile
    form_class = EmployerEditProfile
    context_object_name = 'employer'
    template_name = 'accounts/profile/edit_profile.html'
    success_message = 'Success: Profile information updated.'
    success_url = reverse_lazy('accounts:employer-profile-update')

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


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class AddQualificationView(BSModalCreateView):
    """
    Provide employee ability to add qualification/degree
    """
    template_name = 'accounts/profile/add_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Qualification added.'
    success_url = reverse_lazy('accounts:employee-profile-update')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class UpdateQualificationView(BSModalUpdateView):
    """
    Provide employee ability to update qualification/degree
    """
    model = Qualification
    template_name = 'accounts/profile/update_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Degree was updated.'
    success_url = reverse_lazy('accounts:employee-profile-update')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class DeleteQualificationView(BSModalDeleteView):
    """
    Provide employee ability to delete qualification/degree
    """
    model = Qualification
    template_name = 'accounts/profile/delete-qualification.html'
    success_message = 'Success: Degree was deleted.'
    success_url = reverse_lazy('accounts:employee-profile-update')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class AddDocumentView(BSModalCreateView):
    """
    Provide employee ability to add document
    """
    template_name = 'accounts/profile/add_document.html'
    form_class = DocumentForm
    success_message = 'Success: Document added.'
    success_url = reverse_lazy('accounts:employee-profile-update')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class UpdateDocumentView(BSModalUpdateView):
    """
    Provide employee ability to update document
    """
    model = Document
    template_name = 'accounts/profile/update_document.html'
    form_class = DocumentForm
    success_message = 'Success: Document Updated.'
    success_url = reverse_lazy('accounts:employee-profile-update')


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(is_employee, name='dispatch')
class DeleteDocumentView(BSModalDeleteView):
    """
    Provide employee ability to delete document
    """
    model = Document
    template_name = 'accounts/profile/delete_document.html'
    success_message = 'Success: Document was deleted.'
    success_url = reverse_lazy('accounts:employee-profile-update')
