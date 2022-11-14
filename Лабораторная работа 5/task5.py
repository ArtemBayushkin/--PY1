import random
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(length=8, uppercase=True, punctuation=True):
    str_ = ascii_lowercase
    if uppercase:
        str_ += ascii_uppercase
    if punctuation:
        str_ += digits
    return ''.join(random.sample(str_, length))


print(get_random_password())
