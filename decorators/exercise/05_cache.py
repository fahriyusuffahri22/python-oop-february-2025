def cache(func):
    def wrapper(n):
        if n not in wrapper.log:
            wrapper.log[n] = func(n)

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper
