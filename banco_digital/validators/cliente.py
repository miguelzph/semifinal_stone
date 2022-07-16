from rest_framework.serializers import ValidationError


def validar_campo_numerico(value):
    """Verifica se o campo é númerico. Se for númerico, não retorna nada, 
    e se não for númerico, resulta em erro."""
    if not value.isdigit():
        raise ValidationError("O campo deve conter apenas números")
    
    return None


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError("O campo deve conter apenas números")


def validar_tipo_cpf_cnpj(data):
    """ Verifica as condições de existência entre tipo(pessoa), cpf e cnpj. 
    Se as condições forem garantidas, não retorna nada, 
    caso contrário, resulta em erro.
    
    - Se pessoa física CNPJ deve ser None
    - Se pessoa física CPF NÃO deve ser None
    - Se pessoa jurídica CNPJ NÃO deve ser None
    - Se pessoa jurídica CPF deve ser None
    """
    
    if data.get("tipo") == "PF":
        if data.get("cnpj") is not None:
            raise ValidationError(
                {"cnpj": "Esse campo não deve ser passado para pessoa física"}
            )

        if data.get("cpf") is None:
            raise ValidationError(
                {"cpf": "Esse campo é obrigatório para pessoa física"}
            )

    elif data.get("tipo") == "PJ":
        if data.get("cpf") is not None:
            raise ValidationError(
                {"cpf": "Esse campo não deve ser passado para pessoa jurídica"}
            )

        if data.get("cnpj") is None:
            raise ValidationError(
                {"cnpj": "Esse campo é obrigatório para pessoa jurídica"}
            )

    return None
