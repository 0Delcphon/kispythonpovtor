import math


def main(n, a, b):
    res1 = 0
    for k in range(1, b + 1):
        for i in range(1, a + 1):
            res3 = 1
            for j in range(1, n + 1):
                res3 *= (44*i**5 + (3*j**2 + 1 + 33*k)**6 + (math.ceil(i**3))**3)
            res1 += res3
    return res1


print(main(3, 6, 6))
print(main(7, 6, 8))
print(main(2, 2, 7))
print(main(5, 3, 8))
print(main(5, 8, 3))


