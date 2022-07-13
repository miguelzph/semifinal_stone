from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'email', 'telefone']
        
    # def save(self):
    #     nome = self.validated_data['nome']
    #     cpf = self.validated_data['cpf']
    #     email = self.validated_data['email']
    #     telefone = self.validated_data['telefone']
    #     print(self.data)
        
        
    def validate_telefone(self, telefone):
        return telefone
    
    def validate(self, data):
        if not data.get('telefone').isnumeric(): # poderia usar outros campos
            raise serializers.ValidationError('O campo deve conter apenas números!')
        
        return data
        
            
