from django import forms
from django.forms import ModelForm

from .models import Compra

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = {'item'}