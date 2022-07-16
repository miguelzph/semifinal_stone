from rest_framework.viewsets import GenericViewSet
from banco_digital.models.cliente import Cliente
from banco_digital.serializer.cliente_serializer import ClienteSerializer
from rest_framework.response import Response
from banco_digital.models.conta import Conta
from rest_framework import status
from rest_framework.mixins import CreateModelMixin


class ClienteViewSet(CreateModelMixin, GenericViewSet):
    """ViewSet que permite criar um cliente e adicionar a base."""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):

        if request.data.get("email"):
            request.data["email"] = request.data["email"].lower()

        super().create(request, *args, **kwargs)

        print(request)

        # Criando a conta do cliente
        if request.data["tipo"] == "PF":
            conta = Conta.objects.create(
                cliente=Cliente.objects.get(cpf=request.data["cpf"])
            )
        elif request.data["tipo"] == "PJ":
            conta = Conta.objects.create(
                cliente=Cliente.objects.get(cnpj=request.data["cnpj"])
            )

        request.data["conta"] = conta.conta

        return Response(request.data, status=status.HTTP_201_CREATED)
