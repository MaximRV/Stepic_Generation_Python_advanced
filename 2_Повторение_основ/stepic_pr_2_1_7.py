n = int(input())
result = ''
if len(str(n)) <= 3:
    print(n)
else:
    while len(str(n)) > 3:
        if n % 1000 == 0:
            x = '000'
        else:
              x = n % 1000
        if len(str(n // 1000)) > 3:
            if result == '':
                result = str(x)
            else:
                result = str(x) + ',' + result
        else:
            if result == '':
                result = str(n // 1000) + ',' + str(x)
            else:
                result = str(n // 1000) + ',' + str(x) + ',' + result
        n = n // 1000

print(result)
