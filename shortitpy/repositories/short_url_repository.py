from shortitpy.entities.short_url import ShortURL

class ShortURLsRepository:
    async def create(self, short_url: ShortURL) -> ShortURL :
        pass

    async def getByAccessKey(self, access_key: str) -> ShortURL :
        pass