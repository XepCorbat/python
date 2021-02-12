import math


def formula(q, w):
    return 40 * formula1(q, w) - formula2(q)


def formula1(q, w, k=0):
    for i in range(1, q + 1, 1):
        for j in range(1, w + 1, 1):
            k += (97 * j ** 6 - i ** 3)
    return k


def formula2(q, k=0):
    for i in range(1, q + 1, 1):
        k += (i ** 5 + math.sin(i))
    return k


print("%.2e" % formula(82, 88))
print("%.2e" % formula(91, 73))
