from pytest import raises

from entities.app_error import AppError
from usecases.create_shorturl_usecase import CreateShortURLUseCase

from tests.fixtures.repositories.short_url_repository_in_memory import ShortURLRepositoryInMemory
from tests.fixtures.fake_short_url import make_fake_shortURL


createShortURLUseCase = CreateShortURLUseCase(ShortURLRepositoryInMemory())

class TestCreateShortURLUseCase:

    async def test_invalid_url(self):
        '''Should raise an error for invalid target_url'''

        with raises(AppError, match='Invalid url') as e:
            await createShortURLUseCase.execute('helloworld')


    async def test_valid_url(self):
        '''Should create a short_url and save it on db'''

        short_url_data = make_fake_shortURL()
        short_url = await createShortURLUseCase.execute(short_url_data['target_url'])

        assert short_url_data['target_url'] == short_url.target_url

