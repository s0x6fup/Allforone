import string
import random


def randomString():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12)).lower()
