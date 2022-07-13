from django.contrib import admin

from banco_digital.models.cliente import Cliente
from banco_digital.models.cliente_enderecos import ClienteEnderecos
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.conta import Conta

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    
class ClienteEnderecosAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero','cliente_id')
    
class StatusTransacaoAdmin(admin.ModelAdmin):
    list_display = ('id','status', 'descricao')

class TipoTransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')
    
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_id', 'conta_cliente', 'valor', 'status_id')

class ContaAdmin(admin.ModelAdmin):
    list_display = ('id','saldo')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ClienteEnderecos, ClienteEnderecosAdmin)
admin.site.register(StatusTransacao, StatusTransacaoAdmin)
admin.site.register(TipoTransacao, TipoTransacaoAdmin)
admin.site.register(Transacao, TransacaoAdmin)
admin.site.register(Conta, ContaAdmin)
