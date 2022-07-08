from django.db import models


class StatusTransacao(models.Model):
    status = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.status
    
    class Meta:
        verbose_name_plural = "Status Transacao"


    