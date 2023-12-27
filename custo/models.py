
from django.db import models
from cadastro_animais.models import Animal  # Importe o modelo Animal se ainda não o fez

class Custo(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    categoria = models.CharField('Categoria', max_length=100)
    descricao = models.TextField('Descrição')
    valor = models.DecimalField('Valor (em R$)', max_digits=10, decimal_places=2)
    data_registro = models.DateField('Data de Registro', auto_now_add=True)

    def __str__(self):
        return f'{self.animal.identificacao} - {self.categoria} - {self.data_registro}'
