# Generated by Django 4.0.6 on 2022-07-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banco_digital", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statustransacao",
            name="status",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="tipotransacao",
            name="tipo",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
