from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.serializer.transacao_serializer import TransacaoSerializer


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
