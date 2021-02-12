import math


def formula(n):
    if n == 0:
        return 9
    elif n == 1:
        return 10
    else:
        return math.cos(formula(n - 2)) + 1 / 53 * formula(n - 1) ** 2


print("%.2e" % formula(5))
print("%.2e" % formula(13))
