# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-06-14 12:41
from __future__ import unicode_literals

from django.db import migrations
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_operadorareatrabalho_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operadorareatrabalho',
            name='principal',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, help_text="Se estiver 'Sim', após você salvar, este passa a ser a principal Área de Trabalho do usuário", on=('areatrabalho', 'user'), verbose_name='Principal?'),
        ),
    ]
