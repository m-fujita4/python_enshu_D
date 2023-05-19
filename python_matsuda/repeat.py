import sys
args = sys.argv
# 引数を変数に代入
num = int(args[1])
i = 0
# 100以下の時にループを回す
while i <= 100:
    i = i + num 
    # 100だったらprintしてループを抜け出す  
    if i == 100:
        print("Just 100!",end="")
        break
    # 100未満だったらそのまま通過  
    elif i < 100:
        pass
    # それ以外だったら（100を超えたら）printしてループを抜け出す  
    else: 
        print("Over!",end="")
        break


