from banco_digital.constants.models_constants import (
    STANDART_URL,
    VIEW_CLIENTE_ENDERECOS,
)
from rest_framework.serializers import ValidationError


def validar_ativacao_conta(data):
    """Verifica se a conta_cliente, e caso houver,a conta implicada estão
    liberadas para transaões. Se estiver liberada não retorna nada, e se não
    estiver liberada resulta em erro.

    Args:
        data (Transacao): instancia de uma transacao

    Raises:
        ValidationError: conta_cliente não pode fazer transações
        ValidationError: conta_implicada não pode fazer transações

    Returns:
        None
    """

    if not data.get("conta_cliente").liberada:
        raise ValidationError(
            {
                "conta_cliente": f"""As transações da conta não estão liberadas,
                por favor acesse {STANDART_URL}{VIEW_CLIENTE_ENDERECOS} e 
                complete o cadastro."""
            }
        )

    if data.get("conta_implicada"):
        if not data.get("conta_implicada").liberada:
            raise ValidationError(
                {
                    "conta_implicada": f"""As transações da conta destino não estão 
                    liberadas, por favor peça para que o proprietário acesse 
                    {STANDART_URL}{VIEW_CLIENTE_ENDERECOS} e complete o cadastro."""
                }
            )

    return None
