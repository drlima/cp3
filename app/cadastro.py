from .models import Authentication, User
from .validacoes import validate_user_data, validar_senha


BD: dict[str, list[Authentication | User]] = {
    "auth": [],
    "users": [],
}


def new_user(
    username,
    email,
    nome,
    rg,
    cpf,
    data_de_nascimento,
    endereco,
    role,
    *args,
    **kwargs,
) -> User:
    user = User(
        {
            "id": len(BD["users"]),
            "username": username,
            "email": email,
            "nome": nome,
            "rg": rg,
            "cpf": cpf,
            "data_de_nascimento": data_de_nascimento,
            "endereco": endereco,
            "role": role,
        }
    )
    if not validate_user_data(user):
        raise ValueError("Dados do usuário inválidos")
    return user


def new_auth(user_id, password, *args, **kwargs) -> Authentication:
    if not validar_senha(password):
        raise ValueError("Senha inválida")
    auth = Authentication(
        {
            "user_id": user_id,
            "password": password,
        }
    )
    return auth


def create_new_user(user_data: dict):
    user = new_user(**user_data)
    auth = new_auth(user["id"], user_data.get("password", ""))

    # preencho apenas após a criação com sucesso dos dois objetos
    BD["auth"].append(auth)
    BD["users"].append(user)
