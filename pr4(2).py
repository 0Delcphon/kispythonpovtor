import math


def main(n):
    if n == 0:
        return 0.45
    if n >= 1:
        return main(n-1) + (main(n-1)**2 / 38)


print(main(3))
print(main(8))
print(main(5))
print(main(6))
print(main(2))