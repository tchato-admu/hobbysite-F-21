from django import forms

from.models import Job, JobApplication, Commission


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = "__all__"
        exclude = ["author"]


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ["commission"]