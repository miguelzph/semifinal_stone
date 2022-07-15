from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.cliente import Cliente


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    cliente = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        read_only=False,
        required=False,
        slug_field="nome",
    )

    class Meta:
        model = Conta
        fields = ["conta", "saldo", "cliente"]
