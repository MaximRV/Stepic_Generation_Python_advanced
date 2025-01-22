words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {item : [ord(i) for i in item] for item in words}

print(result)