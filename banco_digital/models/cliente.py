from django.db import models
from localflavor.br.models import BRCPFField
from banco_digital.validators.cliente import validate_cpf
from django.core.validators import validate_email

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = BRCPFField(unique=True, max_length=11, validators=[validate_cpf])
    email = models.CharField(max_length=50, validators=[validate_email], unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome # isso ou adiciona no list field o nome

    class Meta:
        verbose_name_plural = "Cliente"
