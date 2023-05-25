import sys
args = sys.argv

num1=int(args[1])
num2=int(args[2])
num3=int(args[3])

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

        #あまりの値から奇数偶数判定
    if mod != 0:
        return print(str(num) + "は奇数")
    else:
        return print(str(num) + "は偶数")

calcvalue(num1)
calcvalue(num2)
calcvalue(num3)