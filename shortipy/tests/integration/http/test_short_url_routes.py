from fastapi.testclient import TestClient

from shortipy.tests.fixtures.fake_short_url import make_fake_shortURL
from shortipy.tests.fixtures.repositories.short_url_repository_in_memory import ShortURLRepositoryInMemory

from shortipy.infra.http.server import app


class TestShortURLRoutes:
    client = TestClient(app)

    def test_post_create_shorturl(self):
        '''Should return 400 for invalid url'''
        response = self.client.post('/', json={"url": "helloworld"})
        assert response.status_code == 400

    def test_post_create_shorturl1(self):
        """Should return 201 for valid urls"""
        response2 = self.client.post('/', json={"url": "https://google.com"})
        short_url = response2.json()

        assert response2.status_code == 201
        assert response2.headers['content-type'] == 'application/json'
        assert short_url['target_url'] == "https://google.com"

    def test_redirect_by_access_key(self):
        '''Should not redirect user request to a target_url for invalid access key'''
        fake_url_data = make_fake_shortURL()

        response = self.client.get(f"/{fake_url_data.get('access_key')}")

        assert response.status_code == 404

    async def test_redirect_by_access_key1(self):
        '''Should redirect user request to a target_url for valid access key'''
        fake_url_data = make_fake_shortURL()

        short_url_response = self.client.post('/', json={"url": fake_url_data.get('target_url')})
        short_url = short_url_response.json()

        access_key = short_url.get('access_key', '').split('/')
        access_key = access_key.pop()

        response_2 = self.client.get(f"/{access_key}")

        assert response_2.url == short_url.get('target_url')
