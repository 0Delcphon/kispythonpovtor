import math


def main(y):
    if (y < 123):
        return y**6 + y**5 + 1
    if (123 <= y < 220):
        return 75*y**3 + 65*(25+y**3+y)**6
    if (220 <= y < 299):
        return 82 * (89*y)**3 - (85*y**2 - 1)**2
    if (y >= 299):
        return y**3 - math.cos(75*y**2 - 3 - y)**5 - y


print(main(128))
print(main(275))
print(main(103))
print(main(159))
print(main(215))