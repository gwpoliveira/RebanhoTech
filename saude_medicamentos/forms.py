from django import forms
from .models import SaudeMedicamento

class SaudeMedicamentoForm(forms.ModelForm):
    class Meta:
        model = SaudeMedicamento
        fields = ['animal', 'data_registro', 'tipo_registro', 'descricao',
                  'veterinario', 'local_atendimento', 'resultado_exame', 'dose', 'medicamento_utilizado']

