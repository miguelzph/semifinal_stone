from django.db import models
from localflavor.br.models import BRCPFField
from banco_digital.validators.cliente import validate_cpf
import banco_digital.models.conta as model_conta

# signals imports
from django.dispatch import receiver
from django.db.models.signals import post_save

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = BRCPFField(unique=True, max_length=11, validators=[validate_cpf])
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
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
    