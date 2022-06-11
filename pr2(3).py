import math


def main(y):
    if y < 49:
        return 70 * y**2  - math.sqrt(y)
    if 49 <= y < 89:
        return 1 + 20*y**4 + 14 * math.log10(y)**5
    if y >= 89:
        return 1 + y**7 + (y/92)


print(main(46))
print(main(77))
print(main(119))
print(main(130))
print(main(98))