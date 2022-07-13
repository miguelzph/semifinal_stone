from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.cliente import Cliente
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.conta import Conta


class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
    tipo_id = serializers.SlugRelatedField(
        queryset=TipoTransacao.objects.all(),
        read_only=False,
        slug_field='tipo'
    )
    
    conta_cliente = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    

    conta_implicada = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta', required=True
    )
    
    status_id = serializers.SlugRelatedField(
        queryset=StatusTransacao.objects.all(),
        read_only=False,
        slug_field='status', required=False, default=None
    )
    
    class Meta:
        model = Transacao
        fields = ['conta_cliente', 'valor', 'tipo_id', 'status_id', 'conta_implicada']
        lookup_field= 'pk'
