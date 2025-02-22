class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as f:
            f.write(
                f"Function {self.func.__name__} was called. "
                f"Result: {self.func(*args, **kwargs)}\n"
            )
