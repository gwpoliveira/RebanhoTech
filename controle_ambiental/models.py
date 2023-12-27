
from django.db import models

class CondicaoAmbiental(models.Model):
    data_registro = models.DateField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    umidade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return f"Registro de {self.data_registro}"

