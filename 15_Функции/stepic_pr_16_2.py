def pretty_print(data, side='-', delimiter='|'):
    len_object = 0
    for i in data:
        len_object += len(str(i))
    print(" " + side * (len_object + len(data) * 3 -1))
    for i in data:
        print(delimiter,i, end=" ")
    print(delimiter)
    print(" " + side * (len_object + len(data) * 3 -1))

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
