def fibonacci():
    first, second = 0, 1

    while True:
        yield first
        first, second = second, first + second