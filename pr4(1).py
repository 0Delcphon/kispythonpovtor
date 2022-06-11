import math


def main(n):
    if n == 0:
        return 0.33
    if n == 1:
        return 0.29
    if n >= 2:
        return 67*math.atan(main(n-1))**2 + 43*math.atan(main(n-2))**3 + 1


print(main(5))
print(main(6))
print(main(8))
print(main(7))
print(main(2))