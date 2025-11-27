import time
from functools import wraps

def retry(attempts=3, delay=2, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            err = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    err = e
                    print(f"[Retry] {func.__name__} failed (attempt {attempt}/{attempts}). Retrying...")
                    time.sleep(delay)
            raise err
        return wrapper
    return decorator
