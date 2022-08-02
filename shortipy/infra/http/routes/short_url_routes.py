from dataclasses import dataclass
from fastapi import APIRouter, HTTPException

from shortipy.entities.short_url import ShortURL
from shortipy.entities.app_error import AppError
from shortipy.usecases.create_shorturl_usecase import CreateShortURLUseCase
from shortipy.tests.fixtures.repositories.short_url_repository_in_memory import ShortURLRepositoryInMemory

router = APIRouter(
    tags=['short_urls'],
    responses={ 400 : { 'description' : 'Invalid url!' }}
)

fakeShortURLRepo = ShortURLRepositoryInMemory()
createShortURLUseCase = CreateShortURLUseCase(fakeShortURLRepo)


@dataclass
class CreateShortURLPayload:
    url: str


@router.post('/', response_model=ShortURL, status_code=201)
async def create_short_url(payload: CreateShortURLPayload):
    '''Creates a short url'''
    try:
        short_url = await createShortURLUseCase.execute(url=payload.url)
        return short_url
    except AppError as e:
        raise HTTPException(status_code=e.code, detail=e.msg)
