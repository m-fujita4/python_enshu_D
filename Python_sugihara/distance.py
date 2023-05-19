import sys
args = sys.argv
input1 = str(args[1])
input2 = str(args[2])

station = {"東京":0.00, "品川":6.78,"新横浜":25.54, "名古屋":342.02,"京都":476.31, "新大阪":515.35}
if(station[input1]>station[input2]):
    result = station[input1]-station[input2]
    print(round(result,2),end="")
else:
    result = station[input2]-station[input1]
    print(round(result,2),end="")