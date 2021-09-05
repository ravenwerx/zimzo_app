from django import forms
from .models import BusinessModel
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class BusinessModelForm(forms.ModelForm):
    class Meta:
        model = BusinessModel
        fields = '__all__'
        widgets = {
            'business_registered': forms.HiddenInput(),
            'business_name': forms.TextInput(attrs={'class': ''}),
        }
