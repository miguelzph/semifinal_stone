from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.cliente import Cliente
from banco_digital.serializer.cliente_serializer import ClienteSerializer


class ContaSerializer(serializers.HyperlinkedModelSerializer):

    # cliente = serializers.SlugRelatedField(
    #     queryset=Cliente.objects.all(),
    #     read_only=False,
    #     required=True,
    #     slug_field="nome",
    # )

    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Conta
        fields = ["conta", "saldo", "cliente"]
