
from django.db import models
from cadastro_animais.models import Animal

class SaudeMedicamento(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_registro = models.DateField()
    tipo_registro = models.CharField(max_length=50)
    descricao = models.TextField()
    veterinario = models.CharField(max_length=100, blank=True, null=True)
    local_atendimento = models.CharField(max_length=100, blank=True, null=True)
    resultado_exame = models.TextField(blank=True, null=True)
    dose = models.CharField(max_length=50, blank=True, null=True)
    medicamento_utilizado = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_registro} - {self.animal.identificacao}"

