import math


def main(b, a):
    res1 = 0
    res2 = 0
    for j in range(1, b + 1):
        res1 += ((math.atan(j**3 - j**2)**4) / 51) + 21 * math.atan(j)**7
    for i in range(1, a + 1):
        res2 += (1 + i**6 + i**3)
    return res1 + res2


print(main(2, 2))
print(main(8, 4))
print(main(6, 6))
print(main(7, 2))
print(main(3, 8))