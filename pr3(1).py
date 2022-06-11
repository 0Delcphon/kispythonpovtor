import math


def main(m, a, z, b):
    res1 = 0
    res2 = 0
    for c in range(1, a + 1):
        for k in range(1, m + 1):
            res1 += (k**4 - (z+20*k**2)**2 - math.log10(c)**3)
    for k in range(1, a + 1):
        for c in range(1, b + 1):
            res2 += ((1-k**3-c)**5) / 30
    return res1 + res2


print(main(7, 7, 0.43, 4))
print(main(4, 4, 0.81, 7))
print(main(3, 7, -0.48, 5))
print(main(5, 6, -0.39, 5))
print(main(5, 4, 0.59, 8))
