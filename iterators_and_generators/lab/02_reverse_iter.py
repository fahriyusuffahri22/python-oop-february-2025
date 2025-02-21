class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 0:
            raise StopIteration

        self.i -= 1
        return self.iterable[self.i]