def merge(values: list):
    values_dict = {}
    for dict_el in values:
        for key in dict_el:
            if key not in values_dict:
                values_dict[key] = set()
            values_dict[key].add(dict_el[key])
    return values_dict


print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50},
             {'a': 5, 'd': 777}]))
