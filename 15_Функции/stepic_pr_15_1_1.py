def matrix(m=1, n = None, value =0):
    if n:
        return [[value]*n for _ in range(m)]
    return [[value] * m for _ in range(m)]
