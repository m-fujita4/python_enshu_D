import sys
args = sys.argv
input1 = str(args[1]) #第一引数を代入
input2 = int(args[2]) #第二引数を代入
input1 = input1.split(" ") #空白でリストを分割
print(input1[input2-1],end="") #出力