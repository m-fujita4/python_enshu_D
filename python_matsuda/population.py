import sys
args = sys.argv
# 引数を変数に代入
num = int(args[1])-1
# タプルの生成
ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
# 出力
print(ranking[num],end="")