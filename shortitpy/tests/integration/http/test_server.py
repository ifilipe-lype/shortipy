import pytest
from fastapi.testclient import TestClient

from shortitpy.infra.http.server import app

@pytest.mark.integration
def test_ping_pong():
    client = TestClient(app)

    response = client.get('/ping')

    assert response.status_code == 200
    assert response.json() == { 'msg' : 'pong'}