import math


def main(y, z):
    a = (64*y**6+87*math.log2(z)**5) / ((math.acos(y)/86) - ((y**2-(z**3/54)-z)**7 / 91))
    b = 19*math.ceil((z**3/20)+z**2) - (89*y)**7
    return a - math.sqrt(b)


print(main(-0.01, 0.91))