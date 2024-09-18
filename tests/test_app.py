from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_create_user_already_registered_username(client):
    # Primeiro, cria o usuário com sucesso
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    # Tenta criar o mesmo usuário novamente, o que deve falhar
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice2@example.com',  # mesmo username, mas outro email
            'password': 'secret2',
        },
    )

    # Verifica se o status code é 400 (Bad Request)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    # Verifica se a resposta contém a mensagem de erro correta
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_already_registered_email(client):
    # Primeiro, cria o usuário com sucesso
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    # Tenta criar o mesmo usuário novamente, o que deve falhar
    response = client.post(
        '/users/',
        json={
            'username': 'joao',
            'email': 'alice@example.com',  # mesmo username, mas outro email
            'password': 'secret2',
        },
    )

    # Verifica se o status code é 400 (Bad Request)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    # Verifica se a resposta contém a mensagem de erro correta
    assert response.json() == {'detail': 'Email already exists'}


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
