# In your forms.py file within the myapp app

from django import forms
from .models import donor_info

class donorInfoForm(forms.ModelForm):
    class Meta:
        model = donor_info
        fields = '__all__'

