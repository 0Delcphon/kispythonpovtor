import math


def main(n):
    if n == 0:
        return -0.21
    if n >= 1:
        return math.tan(98 - (main(n-1) / 29) - main(n-1)**3)**2 - main(n - 1) - 1


print(main(6))
print(main(1))
print(main(4))
print(main(7))
print(main(5))