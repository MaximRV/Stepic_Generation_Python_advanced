line = input()
n = len(line)
coast = 60
price_rub = (60 * n) // 100
price_kop = (60 * n) % 100
print(price_rub, 'р.', price_kop, 'коп.')
