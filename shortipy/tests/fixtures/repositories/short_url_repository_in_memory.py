from venv import create
from repositories.short_url_repository import ShortURLsRepository
from entities.short_url import ShortURL


class ShortURLRepositoryInMemory(ShortURLsRepository):

    data = []

    def create(self, short_url: ShortURL):
        self.data.append(short_url)

        return short_url