from random import sample
from string import ascii_letters, digits

def get_random_password(n=8) -> str:
    return "".join(sample(ascii_letters + digits, n))

print(get_random_password())
