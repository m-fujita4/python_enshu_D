import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv
# 引数を変数に代入
name1 = args[1]
name2 = args[2]
# 辞書型を生成
distance = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
# -にならないようにする処理
if distance[name2] >distance[name1]:
    kyori = distance[name2] - distance[name1]
else:
    kyori = distance[name1] - distance[name2]
# 小数点第2位まで
kyori = Decimal(str(kyori)).quantize(Decimal("0.00"),rounding = ROUND_HALF_UP)
# 出力
print(kyori,end="")