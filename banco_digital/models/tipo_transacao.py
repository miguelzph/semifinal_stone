from django.db import models


class TipoTransacao(models.Model):
    """Classe que representa os possíveis Tipos de uma transação

    Ex: transferencia; saque

    Args:
        operacao:
            - debito se a operação é de retirada de dinheiro da conta;
            - credito se a operação adiciona dinheiro na conta
        id_tipo_espelho:
            - se none a o tipo de transação não gera transação espelho;
            - se diferente de None (=valor) gera a transação espelho do tipo valor
    """

    debito = "debito"
    credito = "credito"

    OPERACAO_CHOICES = [(debito, "debito"), (credito, "credito")]

    tipo = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=200)
    operacao = models.CharField(choices=OPERACAO_CHOICES, max_length=8)
    id_tipo_espelho = models.ForeignKey(
        "self", default=None, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.tipo

    class Meta:
        verbose_name_plural = "Tipo Transacao"
