from rest_framework import serializers
from banco_digital.models.cliente_enderecos import ClienteEnderecos
from banco_digital.models.cliente import Cliente


class ClienteEnderecosSerializer(serializers.HyperlinkedModelSerializer):

    cliente_id = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        read_only=False,
        required=True,
        slug_field="email",
    )

    class Meta:
        model = ClienteEnderecos
        fields = [
            "cliente_id",
            "cep",
            "rua",
            "numero",
            "bairro",
            "complemento",
            "cidade",
            "estado",
            "pais",
        ]
