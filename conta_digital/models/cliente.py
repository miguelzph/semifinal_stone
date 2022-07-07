from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    saldo = models.FloatField()
    conta = models.CharField(max_length=10)
    telefone = models.CharField(max_length=11)
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome # isso ou adiciona no list field o nome

    class Meta:
        verbose_name_plural = "Cliente"

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
        
        
class TipoTransacao(models.Model):
    tipo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Tipo Transacao"


class StatusTransacao(models.Model):
    status = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.status
    
    class Meta:
        verbose_name_plural = "Status Transacao"


class Transacoes(models.Model):
    cliente_envio_id = models.ForeignKey(Cliente,null=True, related_name='cliente_envio_id', on_delete=models.CASCADE)
    cliente_recebedor_id = models.ForeignKey(Cliente,null=True, related_name='cliente_recebedor_id', on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE) 
    status_id = models.ForeignKey(StatusTransacao, on_delete=models.CASCADE, default=4)
    valor = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    #data_agendamento = 'alo'
    data_ultima_mudanca = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.tipo_id} - {self.valor} - {self.data_criacao}'
    
    class Meta:
        verbose_name_plural = "Transacoes"
