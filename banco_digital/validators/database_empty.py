from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao

def fill_status():
    pass

def correct_status_empty():
    try:
        status = StatusTransacao.objects.get(
                status=STATUS["aguardando_aprovacao"]["status"])
    except:
        populate_status()
        

def populate_status(status: dict):
    """Popula a tabela de status com base em um dicionário

    Args:
        status (dict): dicionário com todos os status do banco de dados
    """
    for _,stat in status.items():

        StatusTransacao.objects.create(
            status=stat['status'],
            descricao=stat['descricao']
        )

        return None
    
    
def populate_status(status: dict):
    """Popula a tabela de status com base em um dicionário

    Args:
        status (dict): dicionário com todos os status do banco de dados
    """
    for _,stat in status.items():

        StatusTransacao.objects.create(
            status=stat['status'],
            descricao=stat['descricao']
        )

        return None



