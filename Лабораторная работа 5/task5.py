import random
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(number=8) -> str:
    str_ = ascii_uppercase + ascii_lowercase + digits
    return "".join(random.sample(str_,number))

print(get_random_password())
