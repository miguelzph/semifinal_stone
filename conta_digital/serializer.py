from django.urls import path, include
from rest_framework import serializers
from conta_digital.models.cliente import Cliente
from conta_digital.models.tipo_transacao import TipoTransacao
from conta_digital.models.transacoes import Transacoes
from conta_digital.models.status_transacao import StatusTransacao


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'saldo', 'conta', 'telefone']
      
 
class TransacoesSerializer(serializers.HyperlinkedModelSerializer):
    tipo_id = serializers.SlugRelatedField(
        queryset=TipoTransacao.objects.all(),
        read_only=False,
        slug_field='tipo'
    )
    
    cliente_envio_id = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    cliente_recebedor_id = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    status_id = serializers.SlugRelatedField(
        queryset=StatusTransacao.objects.all(),
        read_only=False,
        slug_field='status', required=False
    )
    
    class Meta:
        model = Transacoes
        fields = ['url','cliente_envio_id', 'cliente_recebedor_id', 'valor', 'tipo_id', 'status_id']

