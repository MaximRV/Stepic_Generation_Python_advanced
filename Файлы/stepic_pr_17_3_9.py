def read_csv():
    with open('C:\\Users\\Максим\\data.csv', encoding='utf-8') as file:
        row_keys = file.readline().strip().split(',')
        row_values =[row.split(",") for row in file.read().splitlines()]
        result = []
        for row in row_values:
            result.append({row_keys[i]: row[i] for i in range(len(row_keys))})
        return result


print(read_csv())
