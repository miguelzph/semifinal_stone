from django.db import models
from localflavor.br.models import BRCPFField, BRCNPJField
from banco_digital.validators.cliente import validate_cpf, validar_campo_numerico
import banco_digital.models.conta as model_conta

# signals imports
from django.dispatch import receiver
from django.db.models.signals import post_save

class Cliente(models.Model):
    
    pessoa_fisica = 'PF'
    pessoa_juridica = 'PJ'
    
    CLIENTE_TIPO_CHOICES = [(pessoa_fisica, 'PF'),
                        (pessoa_juridica, 'PJ')]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=CLIENTE_TIPO_CHOICES, null=False)
    cpf = BRCPFField(max_length=11, null=True, blank=True, validators=[validar_campo_numerico])
    cnpj = BRCNPJField(max_length=14, null=True, blank=True, validators=[validar_campo_numerico])
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, validators=[validar_campo_numerico])
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome # isso ou adiciona no list field o nome

    class Meta:
        verbose_name_plural = "Cliente"

@receiver(post_save, sender=Cliente)
def cliente_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.email)
        model_conta.Conta.objects.create(cliente=instance)
    