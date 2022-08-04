from shortipy.entities.app_error import AppError
from shortipy.entities.short_url import ShortURL
from shortipy.repositories.short_url_repository import ShortURLsRepository


class GetShortURLByKeyUsecase:
    def __init__(self, shortURLsRepo: ShortURLsRepository) -> None:
        self.shortURLsRepo = shortURLsRepo

    async def execute(self, access_key: str) -> ShortURL:
        short_url = await self.shortURLsRepo.getByAccessKey(access_key=access_key)

        if not short_url:
            raise AppError('Link not found!', 404)
        
        return short_url
