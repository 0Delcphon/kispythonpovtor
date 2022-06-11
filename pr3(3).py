import math


def main(b, n, a):
    res1 = 0
    res3 = 1
    for j in range(1, n + 1):
        for c in range(1, b + 1):
            res1 += ((34 * j + 41)**4 - 93*(c + 79 + c**3)**5)
    for k in range(1, a + 1):
        res2 = 0
        for c in range(1, b + 1):
            res2 += (22 * (c-8)**5 - 86*k - k**4)
        res3 *= res2
    return res1 - res3


print(main(2, 2, 6))
print(main(4, 3, 4))
print(main(8, 2, 3))
print(main(6, 6, 2))
print(main(8, 2, 5))
