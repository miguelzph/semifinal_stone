from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao

     
class DepositoSerializer(serializers.ModelSerializer):
    conta_cliente = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    status_id = serializers.SlugRelatedField(
        queryset=StatusTransacao.objects.all(),
        read_only=False, required=False,
        slug_field='id'
    )
    
    tipo_id = serializers.SlugRelatedField(
        queryset=TipoTransacao.objects.all(),
        read_only=False,
        slug_field='id', required=False
    )
    
    class Meta:
        model = Transacao
        fields = ['conta_cliente', 'valor', 'tipo_id', 'status_id']
        lookup_field= 'pk'
