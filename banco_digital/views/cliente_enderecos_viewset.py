from rest_framework import viewsets
from banco_digital.models.cliente_enderecos import ClienteEnderecos
from banco_digital.serializer.cliente_enderecos_serializer import (
    ClienteEnderecosSerializer,
)


class ClienteEnderecosViewSet(viewsets.ModelViewSet):
    """ViewSet que permite adicionar o endereço do cliente a base."""

    queryset = ClienteEnderecos.objects.all()
    serializer_class = ClienteEnderecosSerializer
