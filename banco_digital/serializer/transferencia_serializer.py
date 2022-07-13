from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao


class TransferenciaSerializer(serializers.ModelSerializer):
    conta_cliente = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    status_id = serializers.SlugRelatedField(
        queryset=StatusTransacao.objects.all(),
        read_only=False, required=False, default=StatusTransacao.objects.get(id=1),
        slug_field='id'
    )
    
    
    tipo_id = serializers.SlugRelatedField(
        queryset=TipoTransacao.objects.all(),
        read_only=False,
        slug_field='id', required=False, default=TipoTransacao.objects.get(id=3)
    )
    
    conta_implicada = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    class Meta:
        model = Transacao
        fields = ['conta_cliente', 'valor', 'conta_implicada', 'tipo_id', 'status_id']
        lookup_field= 'pk'