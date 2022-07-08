from rest_framework import viewsets
from banco_digital.models.transacoes import Transacoes
from banco_digital.serializer.transacoes_serializer import TransacoesSerializer


class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer
