from datetime import date
#モジュールがとのimport
import sys
args = sys.argv
input1 = str(args[1])
input2 = int(args[2])
input3 = int(args[3])

y = int(input1[0:4])
m = int(input1[4:6])
d = int(input1[6:8])
dt = date(y,m,d)
human = input2
child = input3

if dt.strftime("%a") == "Sun" or dt.strftime("%a") == "Sat":
    price =2400 * human +  1500 * child
else:
    price =2000 * human + 1200 * child

print(price,end="")