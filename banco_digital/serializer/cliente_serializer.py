from django.urls import path, include
from rest_framework import serializers
from banco_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'telefone']
