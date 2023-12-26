from django import forms
from .models import Reproducao

class ReproducaoForm(forms.ModelForm):
    class Meta:
        model = Reproducao
        fields = ['animal', 'data_cobertura', 'data_parto', 'numero_filhotes', 'data_desmama']
