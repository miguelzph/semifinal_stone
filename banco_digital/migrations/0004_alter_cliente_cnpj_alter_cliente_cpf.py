# Generated by Django 4.0.6 on 2022-07-14 00:43

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_digital', '0003_alter_cliente_cnpj_alter_cliente_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=localflavor.br.models.BRCPFField(blank=True, max_length=14, null=True),
        ),
    ]
