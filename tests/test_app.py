from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_crud.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_root_html_deve_retornar_ok_e_html():
    client = TestClient(app)

    response = client.get("/html")

    assert response.status_code == HTTPStatus.OK
    assert "<h1> Olá Mundo </h1>" in response.text
    assert "<title> Nosso olá mundo!</title>" in response.text
    assert "<html>" in response.text
    assert "</html>" in response.text
