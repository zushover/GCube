from contextlib import contextmanager
from time import perf_counter


@contextmanager
def timer():
    start = perf_counter()
    result = {"elapsed": None}
    try:
        yield result
    finally:
        result["elapsed"] = perf_counter() - start
