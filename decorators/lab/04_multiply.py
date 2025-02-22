def multiply(times):
    def decorator(function):
        def wrapper(num):
            return function(num) * times

        return wrapper
    return decorator
