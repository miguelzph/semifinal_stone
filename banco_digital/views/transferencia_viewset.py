from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.serializer.transferencia_serializer import TransferenciaSerializer
from rest_framework import mixins


class TransferenciaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransferenciaSerializer

    def perform_create(self, serializer):
        serializer.save(
            tipo_id=TipoTransacao.objects.get(id=3),
            status_id=StatusTransacao.objects.get(id=3),
        )
