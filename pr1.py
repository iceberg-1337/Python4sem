import math


def f11(x, y):
    return (
            math.sin(math.exp(y) + x * x) -
            math.fabs(y) + 18 +
            (x * x - math.pow(y, 6)) / (24 * math.pow(y, 8) + math.log(y)) +
            math.sqrt((91 * math.pow(x, 5) + math.pow(x, 7)) / (math.exp(x) + 82 * math.pow(y, 6)))
    )


def f12(x):
    if x < 42:
        return math.sin(math.exp(x) + x * x) - math.fabs(x) + 18
    elif x < 107:
        return math.pow(x, 6) - 60 * x
    elif x < 137:
        return math.pow(math.fabs(x) - math.pow(x, 3) + 71, 6) + math.tan(x)
    else:
        return math.pow(65 * math.pow(x, 4) + math.pow(x, 3), 5) + 5


def f13(n, m):
    f1 = 0
    f2 = 0
    for i in range(1, n + 1):
        f1 += (math.sin(i) - 61 * i + 49)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f2 += ((math.pow(i, 7)) / 49 - 19 * math.pow(i, 6))
    return f1 - f2


def f14(n):
    if n == 0:
        return 5
    elif n == 1:
        return 8
    else:
        return math.tan(f14(n - 1)) + (1 / 82) * math.pow(f14(n - 1), 3)
