from django.db import models
from cadastro_animais.models import Animal

class Genealogia(models.Model):
    pai = models.ForeignKey(Animal, related_name='genealogia_pai', on_delete=models.CASCADE, verbose_name='Pai')
    mae = models.ForeignKey(Animal, related_name='genealogia_mae', on_delete=models.CASCADE, verbose_name='Mãe')
    filho = models.ForeignKey(Animal, related_name='genealogia_filho', on_delete=models.CASCADE, verbose_name='Filho',blank=True, null=True)

    def __str__(self):
        return f'{self.filho.identificacao} - Genealogia'


