import math


def main(z):
    if z < 4:
        return z**4 + 99*z**2 - 1 - z + z**2
    if 4 <= z < 96:
        return 66*z - 63*z**3
    if z >= 96:
        return 1 - 70*(72*z**3 - 31*z - 1)**2 - math.sin(z)**6


print(main(60))
print(main(178))
print(main(40))
print(main(56))
print(main(96))