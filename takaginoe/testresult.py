# 数学、国語、英語の得点（整数）を入力し、次に示す2つの合格基準を同時に満たす場合は「合格」、それ以外は「不合格」と出力するプログラムを作成せよ
# （Algorithm Drill 2 類題）
 
# 【合格基準】 
# 1. 3教科とも70点以上、または、合計点数が220点以上 
# 2. 1科目も50点未満がない

import sys
# 標準入力を受け付ける
args = sys.argv
# それぞれの点を変数に入れる
math = int(args[1])
japanese = int(args[2])
english = int(args[3])

# 合計点数を求める
sum = math + japanese + english

if math < 50 or japanese < 50 or english < 50: # 50点未満が一個でもあれば不合格
    print("不合格", end="")
elif sum >= 220: # 合計点が220以上なら合格
    print("合格", end="")
elif math >= 70 and japanese >= 70 and english >= 70: # 全教科70点以上なら合格
    print("合格", end="")
else:
    print("不合格",end="")



