from rest_framework import viewsets
from banco_digital.models.cliente import Cliente
from banco_digital.serializer.cliente_serializer import ClienteSerializer
from rest_framework.response import Response
from banco_digital.models.conta import Conta
from rest_framework import status
from rest_framework import mixins


class ClienteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # def list(self, request, *args, **kwargs): # pode ajuda na listagem das outras
    #     custom_data = {
    #         'list_of_items': ClienteSerializer(self.get_queryset(),many=True).data,  # this is the default result you are getting today
    #         'quote_of_the_day': 'ok'}
    #     return Response(custom_data)

    def create(self, request, *args, **kwargs):

        super().create(request, *args, **kwargs)

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
