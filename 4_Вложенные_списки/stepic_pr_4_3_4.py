def pascal(n):
    result = [1]

    for i in range(1, n):
        elem1 = 1
        for j in range(1, n + 1):
            elem1 = elem1 * j

        elem2 = 1
        for k in range(1, i + 1):
            elem2 = elem2 * k

        elem3 = 1
        for h in range(1, n - i + 1):
            elem3 = elem3 * h

        result.append(elem1 // (elem2 * elem3))

    if n != 0:
        result.append(1)

    return result


n = int(input())
for i in range(n):
    print(*pascal(i))