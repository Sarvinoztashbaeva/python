import datetime
from dateutil.relativedelta import relativedelta
user_bd = input('Enter yor birth date(yyyy-mm-dd): ')
birth_date = datetime.datetime.strptime(user_bd, '%Y-%m-%d')
today = datetime.datetime.today()
if birth_date>today:
    print('U did not born yet')
age = relativedelta(today, birth_date)
print(f'Your are {age.years} years, {age.months} months and {age.days} days old')


import datetime
user_bd = input('Enter yor birth date(yyyy-mm-dd): ')
birth_date = datetime.datetime.strptime(user_bd, '%Y-%m-%d')
today = datetime.datetime.today()
current_year_bd = birth_date.replace(year=today.year)
if current_year_bd<today:
    next_bd = current_year_bd.replace(year=today.year +10)
else:
    next_bd = current_year_bd
days_left = (next_bd-today).days
print(f'Your next birthday is in {days_left} days')


import datetime
todays_day = input('Eneter current date and time(yyyy-mm-dd HH:MM): ')
current_datetime = datetime.datetime.strptime(todays_day, '%Y-%m-%d %H:%M')
hours = int(input('Enter meeting duration(hours): '))
minutes = int(input('Enter meeting duration(minuts): '))
meeting_duration = datetime.timedelta(hours=hours, minutes=minutes)
end_time = current_datetime+ meeting_duration
print(f'Meeting will end at {end_time.strftime('%Y-%m-%d %H:%M')}')

import datetime
import pytz
date_input = input('Enter the date and time(yyyy-mm-dd HH:MM): ')
zone = input('Enter your current timezone: ')
to_zone = input('Enter the timezone to convert to: ')
native_datetime = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M')
from_timezone = pytz.timezone(zone)
target_timezone = pytz.timezone(to_zone)
localized_datetime = from_timezone.localize(native_datetime)
converted_datetime = localized_datetime.astimezone(target_timezone)
print(f"\nOriginal time in {zone}: {localized_datetime.strftime('%Y-%m-%d %H:%M (%Z)')}")
print(f"Converted time in {to_zone}: {converted_datetime.strftime('%Y-%m-%d %H:%M (%Z)')}")

import datetime
import time
target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
print("\nCountdown started...\n")
while True:
    now = datetime.datetime.now()
    remaining = target_time - now
    if remaining.total_seconds() <= 0:
        print("Time is up!")
        break
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\rTime remaining: {days}d {hours:02}h:{minutes:02}m:{seconds:02}s", end="")
    time.sleep(1)

