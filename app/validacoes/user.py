from ..models import User
from .login import email_is_valid, cpf_is_valid, rg_is_valid


user_validations = {
    "email": email_is_valid,
    "cpf": cpf_is_valid,
    "rg": rg_is_valid,
}


def validate_user_data(user: User) -> bool:
    return all(
        map(
            lambda key: user_validations[key](user[key]),  # type: ignore
            user_validations,
        )
    )
