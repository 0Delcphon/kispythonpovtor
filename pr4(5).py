import math


def main(n):
    if n == 0:
        return -0.71
    if n >= 1:
        return 0.01 - (main(n-1) / 21) - (math.tan(main(n-1))**2 / 43)


print(main(2))
print(main(7))
print(main(1))
print(main(4))
print(main(8))