from rest_framework import viewsets

from conta_digital.models.cliente import Cliente
from conta_digital.models.transacoes import Transacoes

from conta_digital.serializer.cliente_serializer import ClienteSerializer
from conta_digital.serializer.transacoes_serializer import TransacoesSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer