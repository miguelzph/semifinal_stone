from django.db import models
from banco_digital.models.conta import Conta
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.status_transacao import StatusTransacao

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from rest_framework import serializers
from django.utils import timezone

class Transacao(models.Model):
    conta_cliente = models.ForeignKey(Conta, related_name='conta_id', on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, null=True) 
    status_id = models.ForeignKey(StatusTransacao, on_delete=models.CASCADE, default=1, null=True)
    valor = models.FloatField()
    conta_implicada = models.ForeignKey(Conta,null=True, related_name='conta_implicada', on_delete=models.CASCADE, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_ultima_alteracao = models.DateTimeField(auto_now_add=True, blank=True)
    data_agendamento = models.DateTimeField(null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f'{self.tipo_id} - {self.valor} - {self.data_criacao}'
    
    class Meta:
        verbose_name_plural = "Transacoes"


def tem_saldo(conta, valor):
    return True if (conta.saldo + valor) > 0 else False


def modificar_valor_saldo(conta, valor):
    conta.saldo = conta.saldo + valor
    conta.save()
    
    return None


def criar_transacao_espelho(transacao):
    Transacao.objects.create(tipo_id=transacao.tipo_id.id_tipo_espelho, 
                                status_id=transacao.status_id,
                                conta_cliente=transacao.conta_implicada,
                                conta_implicada = transacao.conta_cliente,
                                valor=-transacao.valor)


@receiver(pre_save, sender=Transacao)
def transacao_create_handler(sender, instance, *args, **kwargs):

    if instance.status_id.id not in [1, 2]:
        if instance.tipo_id.operacao == 'debito': 
            instance.valor = -instance.valor
        
            if not tem_saldo(instance.conta_cliente, float(instance.valor)):
                instance.status_id = StatusTransacao.objects.get(id=2)
                instance.save()
                raise serializers.ValidationError('A conta não possui saldo suficiente!')

        modificar_valor_saldo(instance.conta_cliente, float(instance.valor))
        
        if instance.tipo_id.id_tipo_espelho is not None:
            # criar operação representativa do cliente que está recebendo
            criar_transacao_espelho(instance)
            
        instance.status_id = StatusTransacao.objects.get(id=1)
    print('aqui',instance.tipo_id.id_tipo_espelho)
    instance.data_ultima_alteracao = timezone.now()
    
            

            
                
