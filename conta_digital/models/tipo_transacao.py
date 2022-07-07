from django.db import models

    
class TipoTransacao(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Tipo Transacao"
