from django.db import models
import banco_digital.models.cliente as model_cliente


class Conta(models.Model):
    cliente = models.OneToOneField(model_cliente.Cliente, on_delete=models.CASCADE, editable=False)
    saldo = models.FloatField(default=0, blank=True)
    status = models.BooleanField(default=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.cliente.nome} - {self.id}' # isso ou adiciona no list field a conta

    class Meta:
        verbose_name_plural = "Contas"
        
    