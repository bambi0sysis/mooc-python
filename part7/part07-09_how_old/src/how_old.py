from datetime import datetime

day = int(input('Data: '))
month = int(input('Month: '))
year = int(input('Year: '))

dob = datetime(year, month, day)
eve = datetime(1999, 12, 31)

difference = eve - dob

if difference.days > 0:
    print(f'You were {difference.days} days old on the eve of the new millennium.')
else:
    print("You weren't born yet on the eve of the new millennium.")