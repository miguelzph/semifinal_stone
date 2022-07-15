STANDART_URL = 'http://127.0.0.1:8000/'

VIEW_CLIENTE_ENDERECOS = 'cliente_enderecos'


STATUS = {
    "agendado": {"status": "agendado", "descricao": "A transação está agendada."},
    "aguardando_aprovacao": {
        "status": "aguardando_aprovacao",
        "descricao": "A transação está sendo validada.",
    },
    "cancelado": {"status": "cancelado", "descricao": "A transação foi cancelada."},
    "finalizado": {
        "status": "finalizado",
        "descricao": "A transação foi finalizada com sucesso.",
    },
}

TIPO = {
    "saque": {
        "tipo": "saque",
        "descricao": "Saque monetário.",
        "operacao": "debito",
        "id_tipo_espelho": None,
    },
    "deposito": {
        "tipo": "deposito",
        "descricao": "Deposito monetário.",
        "operacao": "credito",
        "id_tipo_espelho": None,
    },
    "transferencia_recebimento_INT": {
        "tipo": "transferencia_recebimento_INT",
        "descricao": "Recebimento de dinheiro por transferência interna entre contas.",
        "operacao": "credito",
        "id_tipo_espelho": None,
    },
    "transferencia_envio_INT": {
        "tipo": "transferencia_envio_INT",
        "descricao": "Envio de dinheiro por transferência interna entre contas.",
        "operacao": "debito",
        "id_tipo_espelho": 4,
    },
}
