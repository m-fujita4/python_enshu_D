import sys
args = sys.argv
# 引数を変数に代入
word = str(args[1])
num = int(args[2])
# 空白で区切る
word = word.split(" ")
# 出力
print(word[num-1],end="")