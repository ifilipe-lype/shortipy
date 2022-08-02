from venv import create
from shortipy.repositories.short_url_repository import ShortURLsRepository
from shortipy.entities.short_url import ShortURL


class ShortURLRepositoryInMemory(ShortURLsRepository):

    data = []

    def create(self, short_url: ShortURL):
        self.data.append(short_url)

        return short_url