# movimentacao_animais/forms.py

from django import forms
from .models import MovimentacaoAnimal

class MovimentacaoAnimalForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoAnimal
        fields = ['animal', 'tipo_movimentacao', 'data_movimentacao', 'descricao']
