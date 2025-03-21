from decimal import *

num = Decimal(input())
num_tuple = num.as_tuple().digits
if -1 < num < 1:
    num_tuple += (0,)
    print(max(num_tuple) + min(num_tuple))
else:
    print(max(num_tuple) + min(num_tuple))
