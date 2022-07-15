from rest_framework.serializers import ValidationError


def validar_campo_numerico(value):
    if not value.isdigit():
        raise ValidationError("O campo deve conter apenas números")


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError("O campo deve conter apenas números")


def validar_tipo_cpf_cnpj(data):
    if data.get("tipo").upper() == "PF":
        if data.get("cnpj") is not None:
            raise ValidationError(
                {"cnpj": "Esse campo não deve ser passado para pessoa física"}
            )

        if data.get("cpf") is None:
            raise ValidationError(
                {"cpf": "Esse campo é obrigatório para pessoa física"}
            )

    elif data.get("tipo").upper() == "PJ":
        if data.get("cpf") is not None:
            raise ValidationError(
                {"cpf": "Esse campo não deve ser passado para pessoa jurídica"}
            )

        if data.get("cnpj") is None:
            raise ValidationError(
                {"cnpj": "Esse campo é obrigatório para pessoa jurídica"}
            )

    return None
