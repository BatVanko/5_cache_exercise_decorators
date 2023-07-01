import time
from functools import wraps
def cache(func):
    record = dict()
    @wraps(func)
    def wrapper(n):
        result = func(n)
        if n not in record:
            record[n] = result
        return record[n]
    wrapper.log = record

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))
print(fibonacci.log)


