import random
import string

def Gen_password(length=8):
    characters = string.digits + string.ascii_letters  # + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
