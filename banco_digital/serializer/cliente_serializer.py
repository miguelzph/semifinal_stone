from rest_framework import serializers
from banco_digital.models.cliente import Cliente
from banco_digital.validators.cliente import validar_tipo_cpf_cnpj


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    # def validate_telefone(self, telefone):
    #     return telefone
    
    # def validate(self, data):
    #     if not data.get('telefone').isnumeric(): # poderia usar outros campos
    #         raise serializers.ValidationError('O campo deve conter apenas números!')
        
    #     return data
    
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'cnpj', 'email', 'telefone', 'tipo']
    
    def validate(self, data):
        
        validar_tipo_cpf_cnpj(data)
         
        return data
    
    
        
        
            
