from faker import Faker

from shortipy.helpers.gen_random import random_str

def make_fake_shortURL():
    fake = Faker()

    fake_short_url = {
        'target_url': fake.unique.url(),
        'access_key': random_str(12)
    }

    return fake_short_url
