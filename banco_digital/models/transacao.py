from django.db import models
from banco_digital.models.conta import Conta
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.constants.models_constants import STATUS
from django.dispatch import receiver
from django.db.models.signals import pre_save
from rest_framework import serializers
from django.utils import timezone


class Transacao(models.Model):

    """Classe que representa as transações de uma conta
    Args:
        conta_implicada (Conta): conta para qual a transacao foi alvo
            - se o tipo transação gera débito --> conta_implicada = conta que está enviando
            - se o tipo transação gera crédito --> conta_implicada = conta que está recebendo
            - se None: o tipo de transação não impacta outra conta

    """

    conta_cliente = models.ForeignKey(
        Conta, related_name="conta_id", on_delete=models.CASCADE
    )
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, null=True)
    status_id = models.ForeignKey(
        StatusTransacao, on_delete=models.CASCADE, default=1, null=True
    )
    valor = models.FloatField()
    saldo_pre_operacao = models.FloatField(null=True, blank=True)
    conta_implicada = models.ForeignKey(
        Conta,
        null=True,
        related_name="conta_implicada",
        on_delete=models.CASCADE,
        blank=True,
    )
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_ultima_alteracao = models.DateTimeField(auto_now_add=True, blank=True)
    data_agendamento = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f"{self.tipo_id} - {self.valor} - {self.data_criacao}"

    class Meta:
        verbose_name_plural = "Transacoes"


def tem_saldo(conta, valor):
    """Valida se o cliente possui saldo suficiente para realizer a transação

    Returns:
        bool:True se o cliente possui saldo suficiente, e falso caso não possua
    """
    return True if (conta.saldo + valor) > 0 else False


def modificar_valor_saldo(conta, valor):
    """Modifica o valor do saldo da conta de um cliente

    Args:
        conta (Conta): instancia da conta do cliente
        valor (float): valor da transação

    Returns:
        None
    """
    conta.saldo = conta.saldo + valor
    conta.save()

    return None


def criar_transacao_espelho(transacao):
    """Gera uma transacao espelho, com base em outra instancia de transacao

    Args:
        transacao (Transacao): instancia da que gerará a transação espelho
    """
    Transacao.objects.create(
        tipo_id=transacao.tipo_id.id_tipo_espelho,
        status_id=transacao.status_id,
        conta_cliente=transacao.conta_implicada,
        conta_implicada=transacao.conta_cliente,
        valor=-transacao.valor,
    )

    return None


@receiver(pre_save, sender=Transacao)
def transacao_create_handler(sender, instance, *args, **kwargs):
    """Antes de salvar a transacao no Banco de Dados, realiza algumas tarefas:
    - Valida se a transação NÃO está (finalizada ou cancelada)
    - Valida se o cliente possui saldo suficiente em caso de operação = debito
        - Se não possuir salva a transação como cancelada e erro no request
        - Se possuir, modifica o saldo
    - Verifica e gerá uma transação espelho caso se tipo de transação gere uma

    Args:
        instance (Transacao): instancia de transacao que será adicionada ao banco

    Raises:
        serializers.ValidationError: Cliente não possui saldo

    Obs: Apesar do erro a transação é salva no banco como cancelada
    """

    if instance.status_id.status not in [
        STATUS["finalizado"]["status"],
        STATUS["cancelado"]["status"],
    ]:
        instance.saldo_pre_operacao = instance.conta_cliente.saldo

        if instance.tipo_id.operacao == "debito":
            instance.valor = -instance.valor

            if not tem_saldo(instance.conta_cliente, float(instance.valor)):
                instance.status_id = StatusTransacao.objects.get(
                    status=STATUS["cancelado"]["status"]
                )
                instance.save()
                raise serializers.ValidationError(
                    {"saldo": "A conta não possui saldo suficiente!"}
                )

        modificar_valor_saldo(instance.conta_cliente, float(instance.valor))

        if instance.tipo_id.id_tipo_espelho is not None:
            # criar operação representativa do cliente que está recebendo
            criar_transacao_espelho(instance)

        instance.status_id = StatusTransacao.objects.get(
            status=STATUS["finalizado"]["status"]
        )

    instance.data_ultima_alteracao = timezone.now
