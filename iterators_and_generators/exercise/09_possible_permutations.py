from itertools import permutations


def possible_permutations(elements):
    yield from (list(x) for x in permutations(elements))