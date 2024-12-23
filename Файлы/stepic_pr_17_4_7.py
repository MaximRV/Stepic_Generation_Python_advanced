from datetime import datetime

with open('logfile.txt', encoding='utf8') as file:
    rows = [i.strip().split(', ') for i in file.readlines()]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    for row in rows:
        time_format = "%H:%M"
        time1 = datetime.strptime(f'{row[2]}', time_format)
        time2 = datetime.strptime(f'{row[1]}', time_format)
        time_difference = time1 - time2
        if time_difference.total_seconds() / 60 >= 60:
            print(row[0], file=outfile)
