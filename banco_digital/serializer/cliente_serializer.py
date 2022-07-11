from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'telefone']
        
    def validate_telefone(self, telefone):
        return telefone
    
    def validate(self, data):
        if not data.get('telefone').isnumeric(): # poderia usar outros campos
            raise serializers.ValidationError('O campo deve conter apenas números!')
        
        return data
        
            
