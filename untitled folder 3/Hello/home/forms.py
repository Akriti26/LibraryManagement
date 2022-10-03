from pyexpat import model
from attr import fields
from django.core import validators
from django import forms
from .models import Registration

class StudentRegistration(forms.ModelForm):
    class Meta:
        model= Registration
        fields = ['name', 'email', 'password']
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
                                                 
        }