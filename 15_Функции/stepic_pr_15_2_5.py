def print_products(*args):
    prod_list = [i for i in args if type(i) == str and i]
    if prod_list:
        for j in range(len(prod_list)):
            print(f"{j+1}) {prod_list[j]}")
    else:
        print("Нет продуктов")
