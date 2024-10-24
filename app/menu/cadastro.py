from datetime import date

from ..models import Authentication, User, bd
from ..models.user import Role
from ..validacoes import validate_user_data, validar_senha
from ..validacoes.login import (
    username_is_valid,
    email_is_valid,
    rg_is_valid,
    cpf_is_valid,
)


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
            "id": len(bd["users"]),
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


def create_new_user(user_data: dict) -> bool:
    try:
        user = new_user(**user_data)
    except ValueError as e:
        print("Erro ao criar usuário", e)
        return False
    try:
        auth = new_auth(user["id"], user_data.get("password", ""))
    except ValueError as e:
        print("Erro ao criar autenticação", e)
        return False

    # preencho apenas após a criação com sucesso dos dois objetos
    bd["auth"].append(auth)
    bd["users"].append(user)
    return True


def _get_and_validate_data(field_name, validation_function):
    while True:
        data = input(f"Digite um valor para o campo {field_name}: ")
        try:
            if validation_function(data):
                return data
        except Exception as e:
            print(f"Erro ao validar dado {field_name} ", e)
            continue


def _get_user_data():
    return {
        "username": _get_and_validate_data("Username", username_is_valid),
        "email": _get_and_validate_data("Email", email_is_valid),
        "nome": _get_and_validate_data("Nome", lambda x: len(x) > 0),
        "rg": _get_and_validate_data("RG", rg_is_valid),
        "cpf": _get_and_validate_data("CPF", cpf_is_valid),
        "data_de_nascimento": _get_and_validate_data(
            "Data de nascimento [YYYY-MM-DD]",
            lambda x: date.fromisoformat(x),
        ),
        "endereco": _get_and_validate_data("Endereço", lambda x: len(x) > 0),
        "role": Role.USER,
        "password": _get_and_validate_data("Senha", validar_senha),
    }


def menu_cadastro():
    print("Cadastrando um usuário")
    user_created = create_new_user(_get_user_data())
    if user_created:
        print("Usuário cadastrado com sucesso")
        print("user", bd["users"][-1])
        print("user_auth", bd["auth"][-1])
    else:
        print("Erro ao cadastrar usuário")
