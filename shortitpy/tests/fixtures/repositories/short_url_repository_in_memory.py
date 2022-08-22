from venv import create
from shortitpy.repositories.short_url_repository import ShortURLsRepository
from shortitpy.entities.short_url import ShortURL


class ShortURLRepositoryInMemory(ShortURLsRepository):

    data = {}

    async def create(self, short_url: ShortURL):
        self.data[short_url.access_key] = short_url;

        return short_url
    
    async def getByAccessKey(self, access_key: str) -> ShortURL:
        return self.data.get(access_key)