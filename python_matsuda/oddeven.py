import sys
args = sys.argv
# 引数を変数に代入
num = int(args[1])
# if文
if num % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")

# 別解
# num = int(input("数字を入力してください"))
# if num % 2 == 0:
#     print("偶数",end="")
# else:
#     print("奇数",end="")