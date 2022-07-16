from rest_framework.serializers import ValidationError
from banco_digital.models import cliente


def validar_campo_numerico(value):
    """Verifica se o campo é númerico. Se for númerico, não retorna nada,
    e se não for númerico, resulta em erro."""
    if not value.isdigit():
        raise ValidationError("O campo deve conter apenas números")

    return None


def validate_cpf(valor):
    return valor


def validar_campo_unico_cliente(campo, valor):
    """Valida se já há um Cliente com o valor igual no campo especificado.

    Args:
        campo (str): campo a ser validado --> ["cpf", "cnpj]
        valor (str): valor do campo
    """
    print(campo, valor)

    if campo == "cpf":
        contagem = cliente.Cliente.objects.filter(cpf=valor).count()
    elif campo == "cnpj":
        contagem = cliente.Cliente.objects.filter(cnpj=valor).count()

    if contagem != 0:
        raise ValidationError({f"{campo}": f"Já existe Cliente com o {campo}={valor}."})

    return None


def validar_tipo_cpf_cnpj(data):
    """Verifica as condições de existência entre tipo(pessoa), cpf e cnpj.
    Se as condições forem garantidas, não retorna nada,
    caso contrário, resulta em erro.
    - PF:
        - CNPJ deve ser None
        - CPF NÃO deve ser None
          - Se o CPF é único
    - PJ:
        - Se pessoa jurídica CPF deve ser None
        - Se pessoa jurídica CNPJ NÃO deve ser None
            - Se o CNPJ é único

    """

    if data.get("tipo") == "PF":
        # NAO DEVE TER
        if data.get("cnpj") is not None:
            raise ValidationError(
                {"cnpj": "Esse campo não deve ser passado para pessoa física"}
            )

        # DEVE TER
        if data.get("cpf") is None:
            raise ValidationError(
                {"cpf": "Esse campo é obrigatório para pessoa física"}
            )

        # E ALEM DE TER DEVE SER UNCO
        else:
            validar_campo_unico_cliente("cpf", data.get("cpf"))

    elif data.get("tipo") == "PJ":
        # NAO DEVE TER
        if data.get("cpf") is not None:
            raise ValidationError(
                {"cpf": "Esse campo não deve ser passado para pessoa jurídica"}
            )

        # DEVE TER
        if data.get("cnpj") is None:
            raise ValidationError(
                {"cnpj": "Esse campo é obrigatório para pessoa jurídica"}
            )
        # E ALEM DE TER DEVE SER UNCO
        else:
            validar_campo_unico_cliente("cnpj", data.get("cnpj"))

    return None
