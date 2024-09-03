import math


def degree(x: int) -> int | float:
    def dg(n: int) -> int | float:
        return n ** x
    return dg


n = int(input())

elem = input()

elms = {"квадрат": degree(2), "куб": degree(3), "корень": degree(0.5), "модуль": abs, "синус": math.sin}

print(elms[elem](n))