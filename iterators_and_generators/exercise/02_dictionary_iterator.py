class dictionary_iter:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.items):
            raise StopIteration

        item = self.items[self.i]
        self.i += 1

        return item