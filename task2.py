import math


def formula(x):
    if x < 39:
        return math.tan((x ** 8 / 50 - 12 * x ** 3 - 78)) + math.tan(math.sin(x))
    elif 39 <= x & x < 76:
        return x ** 8 + math.fabs(x)
    elif x >= 76:
        return 11 * x ^ 7 + x ** 5 - 85


print("%.2e" % formula(49))
print("%.2e" % formula(-21))
