def build_query_string(param_dict):
    param_list = []
    for key in sorted(param_dict):
        param_list.append('='.join((str(key), str(param_dict[key]))))
    return '&'.join(param_list)


print(build_query_string({"per": 14, "page": 7, "color": "red"}))

