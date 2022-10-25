import random
def get_random_password() -> str:
    s = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789"
    return "".join(random.sample(s,8))

print(get_random_password())
