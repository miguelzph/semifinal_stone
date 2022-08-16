from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao


def correct_status_empty(status: dict):
    if not StatusTransacao.objects.count():  # se for 0
        populate_status(status)

    return None


def populate_status(status: dict):
    """Popula a tabela de status com base em um dicionário

    Args:
        status (dict): dicionário com todos os status do banco de dados
    """
    for _, stat in status.items():

        StatusTransacao.objects.create(
            status=stat["status"], descricao=stat["descricao"]
        )

        return None


def correct_tipo_empty(tipo: dict):
    if not TipoTransacao.objects.count():  # se for 0
        populate_tipo(tipo)

    return None


def populate_tipo(tipo: dict):
    """Popula a tabela de tipo com base em um dicionário

    Args:
        tipo (dict): dicionário com todos os tipos do banco de dados
    """
    for _, t in tipo.items():

        TipoTransacao.objects.create(
            tipo=t["tipo"],
            descricao=t["descricao"],
            operacao=t["operacao"],
            id_tipo_espelho=t["id_tipo_espelho"],
        )

        return None
