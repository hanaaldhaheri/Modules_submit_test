import random
import string
from db import init_db, insert_user

def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    return random.choice(names)

def random_phone():
    return "05" + "".join(random.choices(string.digits, k=8))

def random_user_key():
    return "".join(random.choices(string.ascii_letters + string.digits, k=16))


def main():
    init_db()

    for _ in range(5):  # generate 5 users
        name = random_name()
        phone = random_phone()
        user_key = random_user_key()

        insert_user(name, phone, user_key)
        print(f"Inserted: {name}, {phone}, {user_key}")


if __name__ == "__main__":
    main()