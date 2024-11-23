from http import HTTPStatus

from fastapi.testclient import TestClient

from fastdozero.app import app


def test_index():

    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
