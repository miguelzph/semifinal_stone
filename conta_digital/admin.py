from django.contrib import admin

from conta_digital.models.cliente import Cliente
from conta_digital.models.cliente_enderecos import ClienteEnderecos
from conta_digital.models.tipo_transacao import TipoTransacao
from conta_digital.models.transacoes import Transacoes
from conta_digital.models.status_transacao import StatusTransacao

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    
class ClienteEnderecosAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero','cliente_id')
    
class StatusTransacaoAdmin(admin.ModelAdmin):
    list_display = ('id','status', 'descricao')

class TipoTransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')
    
class TransacoesAdmin(admin.ModelAdmin):
    list_display = ('tipo_id', 'cliente_envio_id', 'cliente_recebedor_id', 'valor', 'status_id')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ClienteEnderecos, ClienteEnderecosAdmin)
admin.site.register(StatusTransacao, StatusTransacaoAdmin)
admin.site.register(TipoTransacao, TipoTransacaoAdmin)
admin.site.register(Transacoes, TransacoesAdmin)
