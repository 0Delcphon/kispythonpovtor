import math


def main(x, z, y):
    res = 0
    n = len(z)
    for i in range(1, n+1):
        a = y[n+1-i-1]**3
        b = z[n+1-math.ceil(i/4)-1]**2
        c = x[math.ceil(i/2)-1]
        res += 2 * (a + b + c)**4
    return res


print(main([-0.14, 0.31],
[0.67, 0.52],
[0.28, -0.37]))
print(main([0.96, 0.86],
[-0.12, -0.03],
[0.68, -0.99]))
print(main([-0.43, -0.13],
[0.67, -0.51],
[-0.58, -0.04]))
print(main([-0.09, 0.14],
[0.45, 0.4],
[0.61, 0.83]))
print(main([-0.72, -0.54],
[0.75, -0.92],
[-0.43, 0.15]))
