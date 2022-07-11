from django.db import models
from banco_digital.models.conta import Conta
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.status_transacao import StatusTransacao


class Transacao(models.Model):
    conta_cliente = models.ForeignKey(Conta,null=True, related_name='conta_id', on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE) 
    status_id = models.ForeignKey(StatusTransacao, on_delete=models.CASCADE, default=1)
    valor = models.FloatField()
    conta_implicada = models.ForeignKey(Conta,null=True, related_name='conta_implicada', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    #data_agendamento = 'alo'
    data_ultima_mudanca = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.tipo_id} - {self.valor} - {self.data_criacao}'
    
    class Meta:
        verbose_name_plural = "Transacoes"
