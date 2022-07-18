from rest_framework import serializers
from banco_digital.models.cliente import Cliente
from banco_digital.validators.cliente import (
    validar_tipo_cpf_cnpj,
    validar_campo_unico_cliente,
)


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "cpf", "cnpj", "email", "telefone", "tipo"]

    def validate(self, data):
        validar_tipo_cpf_cnpj(data)

        return data
