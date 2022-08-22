from shortitpy.entities.short_url import ShortURL
from shortitpy.repositories.short_url_repository import ShortURLsRepository


class CreateShortURLUseCase:

    def __init__(self, shortURLsRepo: ShortURLsRepository) -> None:
        self.shortURLsRepo = shortURLsRepo

    async def execute(self, url: str) -> ShortURL:
        short_url = ShortURL(target_url=url)

        return await self.shortURLsRepo.create(short_url)

