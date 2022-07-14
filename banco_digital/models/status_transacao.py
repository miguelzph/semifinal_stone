from django.db import models


class StatusTransacao(models.Model):
    status = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.status
    
    class Meta:
        verbose_name_plural = "Status Transacao"


    