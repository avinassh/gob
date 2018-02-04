from django import forms
from django.forms import ModelForm

from gob.jobs.models import Job


class JobCreateForm(ModelForm):
    company_name = forms.CharField(required=False, max_length=20)
    location = forms.CharField(required=True, max_length=20)
    description = forms.CharField(required=True, max_length=160)
    salary_end = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            return cleaned_data
        salary_start = cleaned_data['salary_start']
        salary_end = cleaned_data.get('salary_end')
        if salary_end and salary_end < salary_start:
            raise forms.ValidationError(
                "Invalid salary range",
                code='invalid_salary',
            )
        return cleaned_data

    class Meta:
        model = Job
        fields = ['company_name', 'description', 'location', 'salary_start',
                  'salary_end']


class JobUpdateForm(JobCreateForm):

    class Meta:
        model = Job
        fields = ['company_name', 'description', 'location', 'salary_start',
                  'salary_end', 'status']
