from django import forms
from .models import Genealogia

class GenealogiaForm(forms.ModelForm):
    class Meta:
        model = Genealogia
        fields = ['pai', 'mae', 'filho']
