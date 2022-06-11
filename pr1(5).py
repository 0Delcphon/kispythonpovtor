import math


def main(x):
    a = x**3+(x**3/74)
    b = (math.cos(x - 58*x**2)**3 - (1 + x + 47*x**2)**7)
    return a - b


print(main(0.63))
print(main(-0.4))
print(main(-0.81))
print(main(0.07))