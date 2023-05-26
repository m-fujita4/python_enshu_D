# 引数１がHolidayテーブルにあるかを確認→日付の列を取得する→リストに入れる→リストにあるか？
# もしあるなら土日の計算
# ないなら日付を区切って曜日判別

import sys
from datetime import date
from database import session # 1.データベースへの接続
from tables import Holiday # 2.テーブル定義

# 引数入力
args = sys.argv
d = args[1]
adult = int(args[2])
child = int(args[3])

# 日付を分ける
year = d[:4]
month = d[4:6]
day = d[6:8]
dt = date(int(year),int(month),int(day))

# Holidayテーブルから日付の列を取得する
holidaylist = session.query(Holiday.holi_date).all() #リスト型が取得できる

list = []
for i in range(len(holidaylist)):
    list.append(holidaylist[i][0])

if (dt in list) == True:
    adult_sum = 2400 * adult
    child_sum = 1500 * child
else:
    #日付から曜日を判別
    wd = dt.strftime("%a")
    # 入園料の計算
    # 土日の場合の計算
    if wd == "Sat" or wd=="Sun" :
        adult_sum = 2400 * adult
        child_sum = 1500 * child
    # 平日の場合の計算
    else:
        adult_sum = 2000 * adult
        child_sum = 1200 * child
    
sum = adult_sum + child_sum
print(sum,end="")