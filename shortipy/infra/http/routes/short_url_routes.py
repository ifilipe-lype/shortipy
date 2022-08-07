import os
from dataclasses import dataclass

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from shortipy.entities.short_url import ShortURL
from shortipy.entities.app_error import AppError
from shortipy.infra.database.repositories.shorturl_redis_repository import ShortURLsRedisRepository
from shortipy.usecases.create_shorturl_usecase import CreateShortURLUseCase
from shortipy.usecases.get_shorturl_by_key_usecase import GetShortURLByKeyUsecase

router = APIRouter(
    tags=['short_urls'],
    responses={400: {'description': 'Invalid url!'}}
)

repo = ShortURLsRedisRepository()
createShortURLUseCase = CreateShortURLUseCase(repo)
getShortURLByKeyUseCase = GetShortURLByKeyUsecase(repo)


@dataclass
class CreateShortURLPayload:
    url: str


@router.post('/', response_model=ShortURL, status_code=201)
async def create_short_url(payload: CreateShortURLPayload):
    '''Creates a short url'''
    try:
        short_url = await createShortURLUseCase.execute(url=payload.url)
        short_url.access_key = f"{os.environ.get('REDIRECTION_BASE_URL')}/{short_url.access_key}"

        return short_url
    except AppError as e:
        raise HTTPException(status_code=e.code, detail=e.msg)


@router.get('/{access_key}')
async def redirectByAccessKey(access_key: str):
    '''redirects user to target url based on access_key'''
    try:
        short_url = await getShortURLByKeyUseCase.execute(access_key)
        return RedirectResponse(short_url.target_url)
    except AppError as e:
        raise HTTPException(status_code=e.code, detail=e.msg)
