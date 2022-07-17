from banco_digital.models.transacao import Transacao
from banco_digital.serializer.lista_conta_transacao_serializer import (
    ListaContaTransacaoSerializer,
)
from rest_framework.generics import ListAPIView
from banco_digital.models.conta import Conta
from django.http import Http404


class ListaContaTransacaoViewSet(ListAPIView):
    """ViewSet que permite visualizar as transações de uma conta."""

    # def list(self, request, *args, **kwargs): # pode ajuda na listagem das outras
    #     custom_data = {
    #         'list_of_items': ClienteSerializer(self.get_queryset(),many=True).data,  # this is the default result you are getting today
    #         'quote_of_the_day': 'ok'}
    #     return Response(custom_data)

    serializer_class = ListaContaTransacaoSerializer

    def get_queryset(self):
        conta_procurada = Conta.objects.filter(conta=self.kwargs["conta_cliente"])
        if conta_procurada:
            queryset = Transacao.objects.filter(conta_cliente=conta_procurada[0])

            return queryset

        else:
            raise Http404({"conta": "A conta não foi encontrada!"})
