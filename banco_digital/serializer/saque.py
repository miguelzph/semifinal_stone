from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao


class SaqueSerializer(serializers.HyperlinkedModelSerializer):
    conta = serializers.SlugRelatedField(
        queryset=Conta.objects.all(),
        read_only=False,
        slug_field='conta'
    )
    
    status_id = 1
    
    tipo_id = 1
    
    class Meta:
        model = Transacao
        fields = ['conta', 'valor']