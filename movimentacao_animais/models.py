# movimentacao_animais/models.py

from django.db import models
from cadastro_animais.models import Animal

class MovimentacaoAnimal(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(max_length=50)
    data_movimentacao = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.animal.identificacao}"