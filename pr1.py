import math


def main(z, x):
    a = (27+z**2-(1+x**3)**7) / (81*(math.floor(1+13*x**3+z))**4)
    b = (z**2 - 67*x**3 - 1)**2 / (75*(z+95*x**3+x**2)**7)
    return a - math.sqrt(b)


print(main(0.39, 0.67))
