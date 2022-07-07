from rest_framework import viewsets
from conta_digital.models.cliente import Cliente
from conta_digital.serializer.cliente_serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    