from django.core.exceptions import ValidationError

def validate_cpf(value):
        if not value.isdigit():
            raise ValidationError('O CPF deve conter apenas números')