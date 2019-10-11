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
            'type': forms.Select(attrs={'class': 'form-control'}),
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

    class Meta:
        model = JobApplication
        fields = ('cover_letter',)
