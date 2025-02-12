size = int(input())

for stars in range(1, size):
    print(f"{' ' * (size - stars)}{' '.join(['*'] * stars)}")

for stars in range(size, 0, -1):
    print(f"{' ' * (size - stars)}{' '.join(['*'] * stars)}")