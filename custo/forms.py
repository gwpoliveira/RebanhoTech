from django import forms
from .models import Custo

class CustoForm(forms.ModelForm):
    class Meta:
        model = Custo
        fields = ['animal', 'categoria', 'descricao', 'valor']
