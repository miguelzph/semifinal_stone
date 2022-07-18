from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.validators.conta import validar_ativacao_conta


class SaqueSerializer(serializers.ModelSerializer):
    conta_cliente = serializers.SlugRelatedField(
        queryset=Conta.objects.all(), read_only=False, slug_field="conta"
    )

    status_id = serializers.SlugRelatedField(
        queryset=StatusTransacao.objects.all(),
        read_only=False,
        required=False,
        slug_field="status",
    )

    tipo_id = serializers.SlugRelatedField(
        queryset=TipoTransacao.objects.all(),
        read_only=False,
        slug_field="tipo",
        required=False,
    )

    valor = serializers.DecimalField(max_digits=None, decimal_places=2, min_value=0.01)

    saldo_pre_operacao = serializers.ReadOnlyField()

    class Meta:
        model = Transacao
        fields = [
            "conta_cliente",
            "valor",
            "saldo_pre_operacao",
            "tipo_id",
            "status_id",
        ]
        lookup_field = "pk"

    def validate(self, data):
        validar_ativacao_conta(data)

        return data
