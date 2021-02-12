import math

x = float (input())
formula = (((15 * x - math.cos(x)) / (x ** 4 - 51 * x ** 6)) + math.sqrt(47 * x ** 7 + x ** 5)-((x ** 8 + x ** 7) / (52 * x ** 7 + (x ** 5 / 69))))
print("%.2e" % formula)