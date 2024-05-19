n = int(input())
m = int(input())
matrix = []
max_elem_li = []
for _ in range(n):
    elem = list(map(int,input().split()))
    max_elem_li.append(max(elem))
    matrix.append(elem)

max_elem = max(max_elem_li)
line_ind = max_elem_li.index(max_elem)
column_ind = matrix[line_ind].index(max_elem)
print(line_ind,column_ind)
