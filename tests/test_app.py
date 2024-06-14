from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # act (ação)

    # assert response.status_code == 200
    assert response.status_code == HTTPStatus.OK  # assert

    # assert response.json() == {'message': 'Olá Mundo!'}  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
