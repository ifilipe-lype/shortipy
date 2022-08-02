from dataclasses import dataclass
from fastapi import APIRouter, HTTPException

from shortipy.entities.short_url import ShortURL
from shortipy.entities.app_error import AppError
from shortipy.infra.database.repositories.shorturl_redis_repository import ShortURLsRedisRepository
from shortipy.usecases.create_shorturl_usecase import CreateShortURLUseCase

router = APIRouter(
    tags=['short_urls'],
    responses={400: {'description': 'Invalid url!'}}
)

redisShortURLsRepo = ShortURLsRedisRepository()
createShortURLUseCase = CreateShortURLUseCase(redisShortURLsRepo)


@dataclass
class CreateShortURLPayload:
    url: str


@router.post('/', status_code=201)
async def create_short_url(payload: CreateShortURLPayload):
    '''Creates a short url'''
    try:
        return await createShortURLUseCase.execute(url=payload.url)
    except AppError as e:
        raise HTTPException(status_code=e.code, detail=e.msg)
