from banco_digital.models.transacao import Transacao
from banco_digital.serializer.lista_conta_transacao_serializer import (
    ListaContaTransacaoSerializer,
)
from rest_framework.generics import ListAPIView
from banco_digital.models.conta import Conta
from django.http import Http404
from rest_framework.exceptions import ValidationError


class ListaContaTransacaoViewSet(ListAPIView):
    """ViewSet que permite visualizar as transações de uma conta."""

    serializer_class = ListaContaTransacaoSerializer

    def get_queryset(self):
        """Filtra por conta do cliente e opcionalmente por data_maxima e minima"""
        conta_procurada = Conta.objects.filter(conta=self.kwargs["conta_cliente"])
        if conta_procurada:
            queryset = Transacao.objects.filter(conta_cliente=conta_procurada[0])

            data_minima = self.request.query_params.get("data_minima")
            data_maxima = self.request.query_params.get("data_maxima")

            if data_minima:
                try:
                    queryset = queryset.filter(data_ultima_alteracao__gte=data_minima)
                except:
                    raise ValidationError(
                        {
                            "data_minima": f"O valor “{data_minima}” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]."
                        }
                    )

            if data_maxima:
                try:
                    queryset = queryset.filter(data_ultima_alteracao__lte=data_maxima)
                except:
                    raise ValidationError(
                        {
                            "data_maxima": f"O valor “{data_maxima}” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]."
                        }
                    )

            return queryset

        else:
            raise Http404({"conta": "A conta não foi encontrada!"})
