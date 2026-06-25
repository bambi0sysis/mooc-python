from datetime import datetime, timedelta

filename = input("Filename: ")
start_date = datetime.strptime(input('Starting date: '), '%d.%m.%Y')
how_long = int(input("How many days: "))
how_long_duration = timedelta(days = how_long - 1)

print('Please type in screen time in minutes on each day(TV computer mobile):')

data = {}
total = 0

for info in range(how_long):
    on_date = (start_date + timedelta(info)).strftime('%d.%m.%Y')
    info = input(f'Screen time {on_date}: ').split()
    total += sum([int(time) for time in info])
    data[on_date] = '/'.join(info)

with open(filename, 'w') as file:
    start = start_date.strftime('%d.%m.%Y')
    end = (start_date + how_long_duration).strftime('%d.%m.%Y')
    file.write(f'Time period: {start}-{end}\n')
    file.write(f'Total minutes: {total}\n')
    file.write(f'Average minutes: {total / how_long}\n')
    for date, screentime in data.items():
        file.write(f'{date}: {screentime}\n')
print(f'Data stored in file {filename}')