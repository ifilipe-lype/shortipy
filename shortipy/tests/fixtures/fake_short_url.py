from faker import Faker

def make_fake_shortURL():
    fake = Faker()

    fake_short_url = {
        'target_url': fake.unique.url()
    }

    return fake_short_url
