def info_kwargs(**kwargs):
    sorted_dict = dict(sorted(kwargs.items()))
    for i in sorted_dict:
        print(f"{i}: {kwargs[i]}")
