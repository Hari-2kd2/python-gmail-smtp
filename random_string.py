import random
import string


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

