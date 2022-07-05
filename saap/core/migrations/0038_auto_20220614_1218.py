# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-06-14 15:18
from __future__ import unicode_literals

from django.db import migrations
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20220614_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operadorareatrabalho',
            name='preferencial',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Se estiver 'Sim', após você salvar, este passa a ser a Área de Trabalho preferencial para o usuário", on=('user',), verbose_name='Preferencial'),
        ),
    ]
