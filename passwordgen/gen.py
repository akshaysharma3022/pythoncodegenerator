import random
import string

def generate_random_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 15

    password = generate_random_password(password_length)
    print("Generated Password:", password)
