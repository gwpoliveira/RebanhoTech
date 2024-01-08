from django.db import models
from cadastro_animais.models import Animal

class Reproducao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_cobertura = models.DateField(blank=True, null=True)
    data_parto = models.DateField(blank=True, null=True)
    numero_filhotes = models.PositiveIntegerField(blank=True, null=True)
    data_desmama = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Reprodução - {self.animal.identificacao}"
