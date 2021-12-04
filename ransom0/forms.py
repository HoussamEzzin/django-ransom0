from django import forms 
from django.forms import ModelForm, fields
from ransom0.models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields=['key']