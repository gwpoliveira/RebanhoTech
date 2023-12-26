
from django.db import models

class Animal(models.Model):
    identificacao = models.CharField('Identificação:',max_length=50, unique=True)
    data_nascimento = models.DateField('Data de Nacimento:')
    raca = models.CharField("Raça:",max_length=50)
    sexo = models.CharField('Sexo:',max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    cor = models.CharField('Cor:',max_length=50)
    marcacoes = models.TextField('Marcações:',blank=True, null=True)
    foto = models.ImageField('Foto:',upload_to='animal_photos/', blank=True, null=True)
    # Adicione outros campos conforme necessário

    def __str__(self):
        return self.identificacao