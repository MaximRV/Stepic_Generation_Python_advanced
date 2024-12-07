with open('C:\\Users\\Максим\\population.txt', encoding='utf-8') as file:
    rows = file.read().splitlines()
    for row in rows:
        country, population = row.split('\t')
        if country.startswith("G") and int(population) > 500000:
            print(country)