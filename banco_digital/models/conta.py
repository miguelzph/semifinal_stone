from django.db import models
import banco_digital.models.cliente as model_cliente
from django.dispatch import receiver
from django.db.models.signals import post_save


class Conta(models.Model):
    cliente = models.OneToOneField(
        model_cliente.Cliente, on_delete=models.CASCADE, editable=False
    )
    conta = models.CharField(max_length=6, blank=True, null=True, editable=False)
    saldo = models.FloatField(default=0, blank=True)
    liberada = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return f"{self.cliente.nome} - {self.conta}"  # isso ou adiciona no list field a conta

    class Meta:
        verbose_name_plural = "Contas"


@receiver(post_save, sender=Conta)
def cliente_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        instance.conta = instance.id + 100000
        instance.save()
