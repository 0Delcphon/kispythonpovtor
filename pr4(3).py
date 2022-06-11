import math


def main(n):
    if n == 0:
        return 0.32
    if n == 1:
        return 0.85
    if n >= 2:
        return main(n-1)**2 - math.cos(main(n-2)**3) - 0.01


print(main(7))
print(main(5))
print(main(3))
print(main(9))
print(main(8))