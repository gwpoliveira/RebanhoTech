# Generated by Django 5.0 on 2023-12-26 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animais', '0001_initial'),
        ('genealogia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genealogia',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='genealogia',
            name='foto_animal',
        ),
        migrations.RemoveField(
            model_name='genealogia',
            name='foto_mae',
        ),
        migrations.RemoveField(
            model_name='genealogia',
            name='foto_pai',
        ),
        migrations.AddField(
            model_name='genealogia',
            name='filho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genealogia_filho', to='cadastro_animais.animal', verbose_name='Filho'),
        ),
        migrations.AlterField(
            model_name='genealogia',
            name='mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genealogia_mae', to='cadastro_animais.animal', verbose_name='Mãe'),
        ),
        migrations.AlterField(
            model_name='genealogia',
            name='pai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genealogia_pai', to='cadastro_animais.animal', verbose_name='Pai'),
        ),
    ]