import sys
args = sys.argv
# 引数を変数に代入
num = int(args[1])
i = 0
while i <= 100:
    i = i + num   
    if i == 100:
        print("Just 100!",end="")
        break
    elif i < 100:
        pass
    else: 
        print("Over!",end="")
        break


