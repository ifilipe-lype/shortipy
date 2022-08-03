from uuid import UUID
from datetime import datetime

from shortipy.entities.short_url import ShortURL
from shortipy.entities.app_error import AppError

from shortipy.tests.fixtures.fake_short_url import make_fake_shortURL

class Test_ShortURL:
    
    def test_target_url(self):
        '''Target url should be valide'''

        try:
            ShortURL(target_url='helloworld')
        except AppError as e:
            assert e.msg == 'Invalid url!'
        
        try:
            ShortURL(target_url='')
        except AppError as e:
            assert e.msg == 'Invalid url!'


    def test_id(self):
        '''Should auto generate a valide id'''

        fake_short_data = make_fake_shortURL()
        short_url = ShortURL(**fake_short_data)

        assert short_url.id is not None
        assert type(short_url.id) == UUID


    def test_access_key(self):
        '''Should auto generate a access key'''

        fake_short_data = make_fake_shortURL()
        short_url = ShortURL(**fake_short_data)

        assert short_url.access_key is not None


    def test_created_at(self):
        '''Should default to current datetime'''
        
        fake_short_data = make_fake_shortURL()
        short_url = ShortURL(**fake_short_data)

        assert short_url.created_at is not None
        assert type(short_url.created_at) == datetime



