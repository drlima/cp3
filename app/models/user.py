from enum import StrEnum
from datetime import date
from typing import TypedDict


class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"


class Endereco(TypedDict):
    rua: str
    numero: int
    complemento: str
    cep: str
    cidade: str
    estado: str
    pais: str


class User(TypedDict):
    id: int
    username: str
    email: str
    nome: str
    rg: str
    cpf: str
    data_de_nascimento: date
    endereco: Endereco
    role: Role
