import math


def main(x, z, y):
    a = (59*z**2+91*y)**6 - 14*(99*x)**5
    b = (y**2-z**3-30*math.log2(45+x**3)**6) / (42*(38*x**2+(y/41)+42*y**3)-(z**4/49))
    return a - b


print(main(0.96, -0.98, -0.36))
