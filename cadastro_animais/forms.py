# cadastro_animais/forms.py
from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['identificacao', 'data_nascimento', 'raca', 'sexo', 'cor', 'marcacoes', 'foto']
