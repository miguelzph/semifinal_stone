from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.serializer.transferencia_serializer import TransferenciaSerializer
from banco_digital.constants.models_constants import STATUS, TIPO
from rest_framework import mixins


class TransferenciaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ViewSet que permite criar uma transacao do tipo transferencia(interna)."""

    queryset = Transacao.objects.all()
    serializer_class = TransferenciaSerializer

    def perform_create(self, serializer):
        serializer.save(
            tipo_id=TipoTransacao.objects.get(
                tipo=TIPO["transferencia_envio_INT"]["tipo"]
            ),
            status_id=StatusTransacao.objects.get(
                status=STATUS["aguardando_aprovacao"]["status"]
            ),
        )
