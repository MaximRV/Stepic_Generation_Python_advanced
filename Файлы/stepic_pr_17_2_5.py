file = open("nums.txt",'r', encoding='utf-8')
numbers = [int(i) for i in file.read().split()]
print(sum(numbers))
file.close()