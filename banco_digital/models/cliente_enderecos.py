from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from banco_digital.models.cliente import Cliente
from banco_digital.models.conta import Conta


class ClienteEnderecos(models.Model):

    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    eh_principal = models.BooleanField(default=True, blank=True)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.rua + ", " + self.numero

    class Meta:
        verbose_name_plural = "Cliente Enderecos"


@receiver(post_save, sender=ClienteEnderecos)
def cliente_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        Conta.objects.filter(cliente=instance.cliente_id).update(liberada=True)
