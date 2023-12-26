from django.db import models
from cadastro_animais.models import Animal

class Pesagem(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_pesagem = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Pesagem - {self.animal.identificacao} - {self.data_pesagem}"
