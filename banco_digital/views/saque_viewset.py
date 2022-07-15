from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.serializer.saque_serializer import SaqueSerializer
from banco_digital.constants.models_constants import STATUS, TIPO
from rest_framework import mixins


class SaqueViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transacao.objects.all()
    serializer_class = SaqueSerializer

    def perform_create(self, serializer):
        serializer.save(
            tipo_id=TipoTransacao.objects.get(tipo=TIPO["saque"]["tipo"]),
            status_id=StatusTransacao.objects.get(
                status=STATUS["aguardando_aprovacao"]["status"]
            ),
        )
