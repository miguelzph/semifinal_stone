from django.db import models
from django.forms import ValidationError
from banco_digital.models.conta import Conta
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.status_transacao import StatusTransacao


class Transacao(models.Model):
    conta_cliente = models.ForeignKey(Conta, related_name='conta_id', on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, null=True) 
    status_id = models.ForeignKey(StatusTransacao, on_delete=models.CASCADE, default=1, null=True)
    valor = models.FloatField()
    conta_implicada = models.ForeignKey(Conta,null=True, related_name='conta_implicada', on_delete=models.CASCADE, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    #data_agendamento = 'alo'
    data_ultima_mudanca = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.tipo_id} - {self.valor} - {self.data_criacao}'
    
    class Meta:
        verbose_name_plural = "Transacoes"
   
# signals imports
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save    

def tem_saldo(conta, valor):
    return True if (conta.saldo + valor) > 0 else False

@receiver(pre_save, sender=Transacao)
def transacao_create_handler(sender, instance, *args, **kwargs):
    print(instance.conta_cliente.saldo)
    if instance.tipo_id.id in [1,3] and instance.status_id.id != 2: 
        instance.valor = -instance.valor
        if not tem_saldo(instance.conta_cliente, instance.valor):
            instance.status_id = StatusTransacao.objects.get(id=2)
            raise ValidationError('A conta não possui saldo suficiente!')
        
        # modificar_valor_conta_cliente(cliente, valor)
        
        # if instance.tipo_id.id == 3:
        #     # criar transferencia representativa do cliente que está recebendo
        #     new_tipo_id = TipoTransacao.objects.get(id=4)
        #     Transacao.objects.create(tipo_id=new_tipo_id, 
        #                              status_id=instance.status_id,
        #                              conta_cliente=instance.conta_implicada,
        #                              conta_implicada = instance.conta_cliente,
        #                              valor=-instance.valor)
            
            

            
                
