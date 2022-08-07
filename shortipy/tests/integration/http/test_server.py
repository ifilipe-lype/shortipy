from fastapi.testclient import TestClient

from shortipy.infra.http.server import app


def test_ping_pong():
    client = TestClient(app)

    response = client.get('/ping')

    assert response.status_code == 200
    assert response.json() == { 'msg' : 'pong'}