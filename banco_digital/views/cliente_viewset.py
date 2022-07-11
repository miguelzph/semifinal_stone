from rest_framework import viewsets
from banco_digital.models.cliente import Cliente
from banco_digital.serializer.cliente_serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    # def create(self, request, *args, **kwargs):
        
    #     cliente = super().create(request, *args, **kwargs)

        
    #     return cliente