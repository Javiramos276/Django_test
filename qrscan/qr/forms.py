from django.forms import ModelForm
from django import forms
from .models import Qr

class QrForm(forms.ModelForm):
    class Meta:
        model = Qr
        fields = ["data", "titulo"]