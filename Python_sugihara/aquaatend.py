from datetime import date
from database import session
from work_tables import Guest
import sys

args = sys.argv
input1 = str(args[1])
input2 = int(args[2])
input3 = int(args[3])

y = int(input1[0:4])
m = int(input1[4:6])
d = int(input1[6:8])
if(session.query(Guest.entry_date).filter_by(entry_date =input1).count() >= 1):
    entry_list = session.query(Guest.entry_date).filter_by(entry_date =input1).count() + 1
else:
    entry_list = 1

guest =Guest(
     seq = entry_list,
     entry_date = input1,
     adult = input2 ,
     child = input3
)
#保存
session.add(guest)
session.commit()