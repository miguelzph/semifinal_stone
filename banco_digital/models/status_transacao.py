from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_migrate


class StatusTransacao(models.Model):
    """Classe que representa os possíveis status de uma transação

    Ex: cancelado, aguardando_aprovacao"""

    status = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.status

    class Meta:
        verbose_name_plural = "Status Transacao"
