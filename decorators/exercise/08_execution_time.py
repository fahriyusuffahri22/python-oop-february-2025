from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()

        return end - start

    return wrapper
