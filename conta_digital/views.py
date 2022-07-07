from rest_framework import viewsets
from conta_digital.models import Cliente, Transacoes
from conta_digital.serializer import ClienteSerializer, TransacoesSerializer
 

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer