from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.constants.models_constants import STATUS, TIPO
from banco_digital.serializer.deposito_serializer import DepositoSerializer

from rest_framework import mixins


class DepositoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transacao.objects.all()
    serializer_class = DepositoSerializer

    def perform_create(self, serializer):
        serializer.save(
            tipo_id=TipoTransacao.objects.get(tipo=TIPO["deposito"]["tipo"]),
            status_id=StatusTransacao.objects.get(
                status=STATUS["aguardando_aprovacao"]["status"]
            ),
        )
