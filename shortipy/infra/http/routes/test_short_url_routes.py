from fastapi.testclient import TestClient

from ..server import app

class TestShortURLRoutes:
    client = TestClient(app)

    def test_post_create_shorturl(self):
        '''Should return 400 for invalid url'''
        response = self.client.post('/', json={ "url": "helloworld"})
        assert response.status_code == 400

        response2 = self.client.post('/', json={ "url": "https://google.com" })
        short_url = response2.json()

        assert response2.status_code == 201
        assert short_url['target_url'] == "https://google.com"
