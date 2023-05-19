import sys
args = sys.argv

name1=args[1]
name2=args[2]

city={"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,
      "京都":476.31,"新大阪":515.35}

result=city[name1]-city[name2]

#距離がマイナスになった時
if result < 0:
    result = result*(-1)

print(round(result,2))