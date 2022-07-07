from django.urls import path, include
from rest_framework import serializers
from conta_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'saldo', 'conta', 'telefone']
