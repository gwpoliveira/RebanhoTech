# Generated by Django 5.0 on 2023-12-22 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro_animais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reproducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cobertura', models.DateField(blank=True, null=True)),
                ('data_parto', models.DateField(blank=True, null=True)),
                ('numero_filhotes', models.PositiveIntegerField(blank=True, null=True)),
                ('data_desmama', models.DateField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_animais.animal')),
            ],
        ),
    ]
