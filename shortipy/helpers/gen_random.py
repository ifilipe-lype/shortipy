import secrets
import string

def random_str(length: int):
    return ''.join(
        (secrets.choice(string.ascii_letters+string.digits) for i in range(length))
    )