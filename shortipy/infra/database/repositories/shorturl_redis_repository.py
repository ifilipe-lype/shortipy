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
        inserted =  self._repo.set(str(short_url.access_key), bytes(str(short_url.dict()).encode()))

        return short_url if inserted else None

    
