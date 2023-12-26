from django import forms
from .models import Pesagem

class PesagemForm(forms.ModelForm):
    class Meta:
        model = Pesagem
        fields = ['animal', 'data_pesagem', 'peso']
