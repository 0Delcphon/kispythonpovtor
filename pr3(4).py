import math


def main(a, m, n, x):
    res = 0
    for j in range(1, n+1):
        for c in range(1, m + 1):
            for i in range(1, a + 1):
                res += 87 + 98 - 60*j + 48*((c/14) + 77*x**2 + (i**3/63))**5
    return res

print(main(8, 6, 3, 0.5))
print(main(3, 2, 3, -0.72))
print(main(5, 7, 2, -0.48))
print(main(2, 3, 6, -0.38))
print(main(4, 7, 4, 0.06))
