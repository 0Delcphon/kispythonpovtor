import math


def main(x, z, y):
    a = (50 * (math.sqrt(y**2 - y**3 - 55*x))**5 + 56*math.sin(z - z**2 - 16*x**3)**4) / ((49*x**2 + z + 54)**3 - (y**5/50))
    b = math.tan(86*z**2+x+y**3) + (9*z**2 + 1) ** 5
    return a - math.sqrt(b)


print(main(-0.25, 0.4, -0.7))
