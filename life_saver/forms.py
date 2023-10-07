# In your `forms.py` file within the `myapp` app

from django import forms
from .models import DonorInfo, BloodGroup

class donorInfoForm(forms.ModelForm):
    blood_group = forms.ModelChoiceField(queryset=BloodGroup.objects.all(), empty_label="Select Blood Group")
    class Meta:
        model = DonorInfo
        fields = '__all__'

class donorfinderForm(forms.Form):
    blood_group = forms.ModelChoiceField(queryset=BloodGroup.objects.all(),label='Blood Group',empty_label="Select Blood Group",
    widget=forms.Select(attrs={'class': 'form-control'}),
    )
