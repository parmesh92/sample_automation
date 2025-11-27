import random
import string

def generate_random_mailbox():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "test"
