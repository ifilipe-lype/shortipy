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
            password=os.environ.get('REDIS_PASSWORD'),
            port=os.environ.get('REDIS_PORT'),
            db=os.environ.get('REDIS_DB'),
            decode_responses=True
        )

    async def create(self, short_url: ShortURL) -> ShortURL:
        short_url_dict = short_url.dict()

        short_url_dict['id'] = str(short_url_dict['id'])
        short_url_dict['created_at'] = str(short_url_dict['created_at'])

        inserted = self._repo.hset(name=short_url.access_key, mapping=short_url_dict)
        if inserted:
            # Set short_url time to live
            self._repo.expire(name=short_url.access_key, time=os.environ.get('SHORT_URL_TTL'))
            return short_url
        
        return None


    async def getByAccessKey(self, access_key: str) -> ShortURL:
        short_url = self._repo.hgetall(name=access_key)

        if not short_url:
            return None

        return ShortURL(**short_url)
