s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
for i in s.split():
    result[i] = result.get(i, 0) + 1

max_count = 0
key_name = ''
for key in result:
    if result[key] > max_count:
        max_count = result[key]
        key_name = key
    elif result[key] == max_count:
        key_name = min(key_name, key)
print(key_name)
