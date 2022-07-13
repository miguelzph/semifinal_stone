from django.db import models
from banco_digital.models.cliente import Cliente

# depois trocar eh_principal para boolean field

class ClienteEnderecos(models.Model):

    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    eh_principal = models.BooleanField(default=True, blank=True)
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
        
