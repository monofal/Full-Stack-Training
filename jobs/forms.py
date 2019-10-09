from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin
from django import forms

from jobs.models import Job, JobApplication


class CreateJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateJobForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].required = True
        self.fields['position'].required = True
        self.fields['location'].required = True

    class Meta:
        model = Job
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'last_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        fields = ('company_name', 'position', 'location', 'description', 'category', 'type', 'last_date',)

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        job.unique_id = '{}_{}_{}'.format(job.company_name, job.position, job.location)
        if commit:
            job.save()
        return job


class ApplyJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ApplyJobForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobApplication
        fields = ('cover_letter',)

    def __str__(self):
        return self.job.position

    def save(self, commit=False):

        if not self.request.is_ajax():
            application = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            application.user = self.request.user
            application.save()
        else:
            application = super(CreateUpdateAjaxMixin, self).save(commit=False)

        return application
