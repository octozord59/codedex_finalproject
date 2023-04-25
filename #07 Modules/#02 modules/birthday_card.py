# #02 of #02 in Modules

import datetime
import bday_messages

today = datetime.date.today()

my_next_birthday = datetime.date(2023, 9, 5)

days_away = my_next_birthday - today

if today == my_next_birthday:
    print(bday_messages)
else:
    print(f'My next birthday is {days_away.days} days away from today!')

