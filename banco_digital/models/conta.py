from django.db import models


class Conta(models.Model):
    conta = models.UUIDField(primary_key=True)
    saldo = models.FloatField()
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.BooleanField()
    
    def __str__(self) -> str:
        return self.conta # isso ou adiciona no list field a conta

    class Meta:
        verbose_name_plural = "Contas"
        
    