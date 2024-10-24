import pytest

from app.validacoes.login import (
    is_in_chars,
    username_is_valid,
    validar_dominio,
    email_is_valid,
    cpf_is_valid,
    rg_is_valid,
    validar_senha,
)


@pytest.mark.parametrize(
    "char, expected",
    [
        ("a", True),
        ("1", True),
        ("_", True),
        ("-", True),
        ("!", False),
        ("", False),
        ("ab", False),
    ],
)
def test_is_in_chars(char, expected):
    assert is_in_chars(char) == expected


@pytest.mark.parametrize(
    "uname, expected",
    [
        ("valid_user", True),
        ("invalid user", False),
        ("user@name", False),
        ("", False),
        ("daniel.lima", True),
        ("user-name", True),
    ],
)
def test_validar_user_name(uname, expected):
    assert username_is_valid(uname) == expected


@pytest.mark.parametrize(
    "domain, expected",
    [
        ("example.com", True),
        ("sub.example.com", True),
        ("example", False),
        ("example..com", False),
        ("example.com.br.ai", False),
        ("", False),
        ("$dominio.com", False),
        (".com", False),
    ],
)
def test_validar_dominio(domain, expected):
    assert validar_dominio(domain) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("user@example.com", True),
        ("user.name@sub.example.com", True),
        ("user@com", False),
        ("user@.com", False),
        ("userexample.com", False),
    ],
)
def test_validar_email(email, expected):
    assert email_is_valid(email) == expected


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("123.456.789-00", True),
        ("12345678900", True),
        ("123.456.789-0", False),
        ("1234567890", False),
        ("123.456.789-000", False),
        ("1234567890000", False),
        ("12.345.678-90", False),
        ("123.45.678-90", False),
        ("123.456.78-90", False),
        ("123456.789-00", False),
    ],
)
def test_validar_cpf(cpf, expected):
    assert cpf_is_valid(cpf) == expected


@pytest.mark.parametrize(
    "rg, expected",
    [
        ("12.345.678-9", True),
        ("123456789", True),
        ("12.345.678-", False),
        ("12345678", False),
        ("1234567890", False),
        ("12.345.6789", False),
        ("123.45.678-9", False),
        ("12.456.78-9", False),
        ("12456.789-0", False),
    ],
)
def test_validar_rg(rg, expected):
    assert rg_is_valid(rg) == expected


@pytest.mark.parametrize(
    "senha, expected",
    [
        ("A1b!A1b!A1b!A1b!", True),
        ("A1b!A1b!A1b!A1", False),  # Less than 15 characters
        ("A1B!A1B!A1b!A1b!", False),  # Not enough lowercase letters
        ("A1b!a1b!a1b!a1b!ab!", False),  # Not enough uppercase letters
        ("A1b!Ab!Ab!Ab!Ab!A1b!", False),  # Not enough digits
        ("A1b!A1b!A1bA1bA1bA1bA1b", False),  # Not enough special characters
    ],
)
def test_validar_senha(senha, expected):
    assert validar_senha(senha) == expected
