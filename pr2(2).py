import math


def main(y):
    if y < -5:
        return (math.ceil(y))**3 + (76*y**2) / 60
    if -5 <= y < 93:
        return 23 * (math.ceil(y**2))**7 + y**4
    if y >= 93:
        return y**3 - 36


print(main(-68))
print(main(29))
print(main(118))
print(main(83))
print(main(-38))