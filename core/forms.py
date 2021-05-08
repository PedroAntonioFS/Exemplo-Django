from django import forms
from django.forms import ModelForm

from .models import lista_de_compras

class lista_de_compra_form(ModelForm):
    class Meta:
        model = lista_de_compras
        field = {'item'}