import re
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase

characters = ascii_letters + digits + "_" + "-" + "."


def is_in_chars(c: str) -> bool:
    return c in characters and len(c) == 1


def username_is_valid(uname: str) -> bool:
    if not len(uname):
        return False
    return all(map(is_in_chars, uname))


def validar_dominio(domain: str) -> bool:
    if "." not in domain:
        return False
    parts = domain.split(".")
    for p in parts:
        if not len(p):
            return False
    if not (2 <= len(parts) <= 3):
        return False
    return all(map(lambda x: all(map(is_in_chars, x)), parts))


def email_is_valid(email: str) -> bool:
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    user, domain = parts
    return username_is_valid(user) and validar_dominio(domain)


def cpf_is_valid(cpf: str) -> bool:
    return any(
        (
            re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf),
            re.fullmatch(r"\d{11}", cpf),
        )
    )


def rg_is_valid(rg: str) -> bool:
    return any(
        (
            re.fullmatch(r"\d{2}\.\d{3}\.\d{3}-\d", rg),
            re.fullmatch(r"\d{9}", rg),
        )
    )


def count_chars_in_pattern(s: str, pattern: str) -> int:
    return len([c for c in s if c in pattern])


def validar_senha(senha: str) -> bool:
    if len(senha) < 15:
        return False

    return all(
        map(
            lambda pattern: count_chars_in_pattern(senha, pattern) >= 3,
            (
                digits,
                ascii_uppercase,
                ascii_lowercase,
                r"!@#$%&*()[]{};,.:/\|",
            ),
        )
    )
