class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = "aeiouAEIOU"
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.text):
            value = self.text[self.i]
            self.i += 1

            if value in self.vowels:
                return value

        raise StopIteration