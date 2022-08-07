import os

import redis
from dotenv import load_dotenv

from shortipy.entities.short_url import ShortURL
from shortipy.repositories.short_url_repository import ShortURLsRepository


load_dotenv()


class ShortURLsRedisRepository(ShortURLsRepository):
    def __init__(self) -> None:
        super().__init__()

        self._repo = redis.Redis(
            host=os.environ.get('REDIS_NETWORK_NAME'),
            port=6379,
            db=0,
            password=os.environ.get('REDIS_PASSWORD')
        )

    async def create(self, short_url: ShortURL) -> ShortURL:
        short_url_dict = short_url.dict()

        short_url_dict['id'] = str(short_url_dict['id'])
        short_url_dict['created_at'] = str(short_url_dict['created_at'])

        inserted = self._repo.hset(name=short_url.access_key, mapping=short_url_dict)

        return short_url if inserted else None

    async def getByAccessKey(self, access_key: str) -> ShortURL:
        short_url = self._repo.hgetall(name=access_key)

        if not short_url:
            return None

        short_url = {str(key, 'utf-8'): str(value, 'utf-8') for key, value in short_url.items()}

        return ShortURL(**short_url)
