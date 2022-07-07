from rest_framework import viewsets
from conta_digital.models.transacoes import Transacoes
from conta_digital.serializer.transacoes_serializer import TransacoesSerializer


class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer
