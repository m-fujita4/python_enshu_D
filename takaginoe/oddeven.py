# 引数で渡した整数が奇数か偶数かを判定

import sys
# 標準入力を受け付けてargsに入れる
args = sys.argv

# 入力がない場合
if len(args) < 2:
    print("error : 入力がありません")
    sys.exit()

# 数字に変換し、変数numに入れる
num = int(args[1])

# 奇数か偶数か判定
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")