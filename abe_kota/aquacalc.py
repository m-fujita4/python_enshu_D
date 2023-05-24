from datetime import date

import sys
args = sys.argv
input_date=args[1]
adults=int(args[2])
children=int(args[3])

year=int(input_date[0:4])
month=int(input_date[4:6])
day=int(input_date[6:8])

dt=date(year,month,day)
weekday=dt.strftime("%a")

print(weekday)

if weekday=="Sat" or weekday=="Sun":
    price=(2400*adults)+(1500*children)

else:
    price=(2000*adults)+(1200*children)

print(price)


#print(input_date.strftime("%Y"))
#print(date.strftime(input_date))



#dt=date(2022,6,4)

#print(dt.strftime("%a"),end="")


