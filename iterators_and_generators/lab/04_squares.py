def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1