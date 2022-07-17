from django.db import models
from localflavor.br.models import BRCPFField, BRCNPJField
from banco_digital.validators.cliente import validar_campo_numerico


class Cliente(models.Model):

    pessoa_fisica = "PF"
    pessoa_juridica = "PJ"

    CLIENTE_TIPO_CHOICES = [(pessoa_fisica, "PF"), (pessoa_juridica, "PJ")]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=CLIENTE_TIPO_CHOICES, null=False)
    cpf = BRCPFField(
        max_length=11, null=True, blank=True, validators=[validar_campo_numerico]
    )
    cnpj = BRCNPJField(
        max_length=14, null=True, blank=True, validators=[validar_campo_numerico]
    )
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, validators=[validar_campo_numerico])
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome} - {self.email}"  # isso ou adiciona no list field o nome

    class Meta:
        verbose_name_plural = "Cliente"
