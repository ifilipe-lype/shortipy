from os import access
from pytest import raises

from shortitpy.entities.app_error import AppError
from shortitpy.tests.fixtures.fake_short_url import make_fake_shortURL
from shortitpy.usecases.create_shorturl_usecase import CreateShortURLUseCase
from shortitpy.usecases.get_shorturl_by_key_usecase import GetShortURLByKeyUsecase
from shortitpy.tests.fixtures.repositories.short_url_repository_in_memory import ShortURLRepositoryInMemory

getShortURLByKeyUsecase = GetShortURLByKeyUsecase(ShortURLRepositoryInMemory())
createShortURLUseCase = CreateShortURLUseCase(ShortURLRepositoryInMemory())


class TestGetShortURLByKeyUsecase:
    async def test_non_existing_access_key(self):
        fake_url_data = make_fake_shortURL()

        with raises(AppError, match='Link not found') as e:
            access_key = fake_url_data.get('access_key')
            await getShortURLByKeyUsecase.execute(access_key)
    

    async def test_existing_access_key(self):
        fake_url_data = make_fake_shortURL()
        short_url = await createShortURLUseCase.execute(fake_url_data.get('target_url'))

        assert fake_url_data.get('target_url') == short_url.target_url

        found_short_url = await getShortURLByKeyUsecase.execute(short_url.access_key)

        assert short_url.access_key == found_short_url.access_key
        assert short_url is found_short_url

