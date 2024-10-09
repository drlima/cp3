from ..models import User
from .login import validar_email, validar_cpf, validar_rg


user_validations = {
    "email": validar_email,
    "cpf": validar_cpf,
    "rg": validar_rg,
}


def validate_user_data(user: User) -> bool:
    return all(
        map(
            lambda key: user_validations[key](user[key]),  # type: ignore
            user_validations,
        )
    )
