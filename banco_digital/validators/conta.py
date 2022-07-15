from banco_digital.constants.models_constants import (
    STANDART_URL,
    VIEW_CLIENTE_ENDERECOS,
)
from rest_framework.serializers import ValidationError


def validar_ativacao_conta(data):

    if not data.get("conta_cliente").liberada:
        raise ValidationError(
            {
                "conta_cliente": f"As transações da conta não estão liberadas,por favor acesse {STANDART_URL}{VIEW_CLIENTE_ENDERECOS} e complete o cadastro."
            }
        )

    if data.get("conta_implicada"):
        if not data.get("conta_implicada").liberada:
            raise ValidationError(
                {
                    "conta_implicada": f"As transações da conta destino não estão liberadas, por favor peça para que o proprietário acesse {STANDART_URL}{VIEW_CLIENTE_ENDERECOS} e complete o cadastro."
                }
            )

    return None
