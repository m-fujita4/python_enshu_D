import sys
args = sys.argv
input1 = str(args[1])
input2 = str(args[2])

#辞書の定義
station = {"東京":0.00, "品川":6.78,"新横浜":25.54, "名古屋":342.02,"京都":476.31, "新大阪":515.35}
try:
    if(station[input1]>station[input2]): 
        result = station[input1]-station[input2] #距離計算
        print(round(result,2),end="")
    else:
        result = station[input2]-station[input1] #距離計算
        print(round(result,2),end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")