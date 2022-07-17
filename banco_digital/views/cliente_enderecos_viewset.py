from banco_digital.models.cliente_enderecos import ClienteEnderecos
from banco_digital.serializer.cliente_enderecos_serializer import (
    ClienteEnderecosSerializer,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin



class ClienteEnderecosViewSet(CreateModelMixin, GenericViewSet):
    queryset = ClienteEnderecos.objects.all()
    serializer_class = ClienteEnderecosSerializer

    def create(self, request, *args, **kwargs):
        """Função que cria um endereco para um cliente"""
        
        # padroniza email minusculo
        if request.data.get("cliente_id"):
            request.data._mutable = True
            request.data["cliente_id"] = request.data["cliente_id"].lower()
            request.data._mutable = False

        return super().create(request, *args, **kwargs)
