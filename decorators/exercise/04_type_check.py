def type_check(args_type):
    def decorator(func):
        def wrapper(*args):
            if all(isinstance(x, args_type) for x in args):
                return func(*args)

            return "Bad Type"

        return wrapper
    return decorator
