import sys
import datetime
args = sys.argv

date = args[1]
adult_num = int(args[2]) 
child_num = int(args[3])
total_fee = 0

# 料金表
weekday_fee = {
    '大人':2000, 
    'こども':1200
}
weekend_fee = {
    '大人':2400, 
    'こども':1500
}

# 入力された日付を分ける
year = date[:4]
month = date[4:6]
day = date[6:]

date = datetime.date(int(year),int(month),int(day))
youbi =  date.weekday()

if youbi == 5 or youbi == 6: # weekend
    total_fee = adult_num * weekend_fee['大人'] + child_num * weekend_fee['こども']
else:
    total_fee = adult_num * weekday_fee['大人'] + child_num * weekday_fee['こども']

print(str(total_fee), end="")