import numpy as np
import string


def generate_random_string(length=10):
    """
    Generates a random string of a given length consisting of ASCII letters, digits, and punctuation.

    :param length: The length of the random string to generate. Defaults to 10.
    :return: A string of random characters with the specified length.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(np.random.choice(list(characters), size=length))
