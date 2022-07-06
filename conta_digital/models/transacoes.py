from conta_digital.models.cliente import Cliente
from conta_digital.models.tipo_transacao import TipoTransacao
from conta_digital.models.status_transacao import StatusTransacao
from django.db import models


class Transacoes(models.Model):
    cliente_envio_id = models.ForeignKey(Cliente,null=True, related_name='cliente_envio_id', on_delete=models.CASCADE)
    cliente_recebedor_id = models.ForeignKey(Cliente,null=True, related_name='cliente_recebedor_id', on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE) 
    status_id = models.ForeignKey(StatusTransacao, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    #data_agendamento = 'alo'
    data_ultima_mudanca = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.tipo_id} - {self.valor} - {self.data_criacao}'
    
    class Meta:
        verbose_name_plural = "Transacoes"

