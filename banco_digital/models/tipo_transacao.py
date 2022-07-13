from django.db import models

    
class TipoTransacao(models.Model):
    debito = 'debito'
    credito = 'credito'
    
    OPERACAO_CHOICES = [(debito, 'debito'),
                        (credito, 'credito')]
    
    tipo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    operacao = models.CharField(choices=OPERACAO_CHOICES, max_length=8)
    id_tipo_espelho = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Tipo Transacao"
