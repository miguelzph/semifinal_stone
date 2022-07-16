from banco_digital.models.transacao import Transacao
from banco_digital.serializer.lista_conta_transacao_serializer import (
    ListaContaTransacaoSerializer,
)
from rest_framework.generics import ListAPIView
from banco_digital.models.conta import Conta


class ListaContaTransacaoViewSet(ListAPIView):
    """ViewSet que permite visualizar as transações de uma conta."""

    def get_queryset(self):
        queryset = Transacao.objects.filter(
            conta_cliente=Conta.objects.filter(conta=self.kwargs["conta_cliente"])[0]
        )

        return queryset

    serializer_class = ListaContaTransacaoSerializer
