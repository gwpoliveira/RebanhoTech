
from django import forms
from .models import CondicaoAmbiental

class CondicaoAmbientalForm(forms.ModelForm):
    class Meta:
        model = CondicaoAmbiental
        fields = ['data_registro', 'temperatura', 'umidade', 'descricao']
