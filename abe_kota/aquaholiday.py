from datetime import date
from database import session
from table import Holiday
import sys

args = sys.argv
input_date=args[1]
adults=int(args[2])
children=int(args[3])

holidaylist=session.query(Holiday.holi_date).all()

year=int(input_date[0:4])
month=int(input_date[4:6])
day=int(input_date[6:8])

dt=date(year,month,day)
weekday=dt.strftime("%a")

print(dt)

for i in range(len(holidaylist)):
    if input_date==holidaylist[i]:
        weekday="public"

if weekday=="Sat" or weekday=="Sun" or weekday=="public" :
    price=(2400*adults)+(1500*children)

else:
    price=(2000*adults)+(1200*children)

print(price)