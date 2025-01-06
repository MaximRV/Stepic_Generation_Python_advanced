row = input().split()
row_elements = {}
for elem in row:
    if elem in row_elements:
        row_elements[elem + f'_{row_elements[elem] + 1}'] = 0
        row_elements[elem] = row_elements.get(elem, 0) + 1
    else:
        row_elements[elem] = 0


print(' '.join(row_elements.keys()))