# forms.py
from django import forms
from .models import Profile
from django import forms
from .models import ServiceRequest


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']


# class ServiceRequestForm(forms.ModelForm):
#     class Meta:
#         model = ServiceRequest
#         fields = ['service_type', 'description', 'attachments']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description']
