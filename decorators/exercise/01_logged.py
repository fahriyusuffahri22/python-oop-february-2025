def logged(func):
    def wrapper(*args):
        return (
            f"you called {func.__name__}{args}\n"
            f"it returned {func(*args)}"
        )

    return wrapper
