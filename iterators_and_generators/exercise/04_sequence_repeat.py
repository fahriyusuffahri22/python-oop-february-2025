class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.number:
            raise StopIteration

        value = self.sequence[self.i % len(self.sequence)]
        self.i += 1

        return value