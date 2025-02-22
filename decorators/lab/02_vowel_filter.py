def vowel_filter(function):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def wrapper():
        return [x for x in function() if x in vowels]

    return wrapper
