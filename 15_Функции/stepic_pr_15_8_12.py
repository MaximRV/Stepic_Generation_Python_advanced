from functools import reduce


def evaluate(coefficients, x):
    numbers_degree= list(range(len(coefficients)-1,-1,-1))
    return reduce(lambda c,d: c + d,map(lambda a,b: a * b, map(lambda y: x**y, numbers_degree),coefficients))


coefficients = list(map(int, input().split()))

x = int(input())


print(evaluate(coefficients, x))
