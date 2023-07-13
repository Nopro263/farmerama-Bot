import random
import string


def randomUsername(lenght: int, start: str = ""):
    return f"{start}{''.join([random.choice(string.ascii_letters + string.digits) for _ in range(lenght - len(start))])}"

def randomPassword(lenght: int):
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(lenght)])
