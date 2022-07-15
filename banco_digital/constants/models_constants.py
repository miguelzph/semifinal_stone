STATUS = [
    {"status": "agendado", "descricao": "A transação está agendada."},
    {"status": "aguardando_aprovacao", "descricao": "A transação está sendo validada."},
    {"status": "cancelado", "descricao": "A transação foi cancelada."},
    {"status": "finalizado", "descricao": "A transação foi finalizada com sucesso."},
]

TIPO = [
    {
        "tipo": "saque",
        "descricao": "Saque monetário.",
        "operacao": "debito",
        "id_tipo_espelho": None,
    },
    {
        "tipo": "deposito",
        "descricao": "Deposito monetário.",
        "operacao": "credito",
        "id_tipo_espelho": None,
    },
    {
        "tipo": "transferencia_recebimento_INT",
        "descricao": "Recebimento de dinheiro por transferência interna entre contas.",
        "operacao": "credito",
        "id_tipo_espelho": None,
    },
    {
        "tipo": "transferencia_envio_INT",
        "descricao": "Envio de dinheiro por transferência interna entre contas.",
        "operacao": "debito",
        "id_tipo_espelho": 4,
    },
]
