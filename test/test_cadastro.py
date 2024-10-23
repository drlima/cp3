from app.menu.cadastro import new_user, new_auth, create_new_user, bd


def test_new_user_valid():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "nome": "Test User",
        "rg": "123456789",
        "cpf": "12345678901",
        "data_de_nascimento": "2000-01-01",
        "endereco": "123 Test St",
        "role": "user",
    }
    user = new_user(**user_data)
    # assert user.__class__ == User
    for key, value in user_data.items():
        assert user[key] == value


def test_new_auth_valid():
    auth = new_auth(user_id=0, password="VDR!!!validpassword123")
    # assert auth.__class__ == Authentication
    assert auth["password"] == "VDR!!!validpassword123"


def test_create_new_user():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "nome": "Test User",
        "rg": "123456789",
        "cpf": "12345678901",
        "data_de_nascimento": "2000-01-01",
        "endereco": "123 Test St",
        "role": "user",
        "password": "VDR!!!validpassword123",
    }
    create_new_user(user_data)
    user = bd["users"][0]
    auth = bd["auth"][0]

    assert len(bd["users"]) == 1
    assert len(bd["auth"]) == 1

    for key, value in user_data.items():
        if key == "password":
            continue
        assert user[key] == value

    assert auth["user_id"] == 0
    assert auth["password"] == "VDR!!!validpassword123"
