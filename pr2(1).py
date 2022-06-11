import math


def main(y):
    if y < -31:
        return 5 * (math.ceil(y**3))**4 + y**5
    if (-31 <= y < 47):
        return (1+y+y**3)**3 + 75 + y**4
    if (47 <= y < 73):
        return y**6 - 7*(0.01 - y**2 - 41*y)**5
    if (y >= 73):
        return y**15 + math.log(y)**2 + 98*y**6


print(main(-53))
print(main(65))
print(main(-6))
print(main(-20))
print(main(-46))