from django.db import models
from conta_digital.models.cliente import Cliente


class ClienteEnderecos(models.Model):
    PRINCIPAL = 'sim'
    NAO_PRINCIPAL = 'nao'
    
    ENDERECO_CHOICES = [(PRINCIPAL, 'sim'),
                        (NAO_PRINCIPAL, 'nao')]
    
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    eh_principal = models.CharField(max_length=3, choices=ENDERECO_CHOICES, default='sim')
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.rua + ', ' + self.numero
   
    class Meta:
        verbose_name_plural = "Cliente Enderecos"
        
