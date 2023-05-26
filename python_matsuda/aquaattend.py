import sys
from datetime import date
from database import session # 1.データベースへの接続
from attendnum_table import Attend # 2.テーブル定義

# 引数入力
args = sys.argv
d = args[1]
adult_num = int(args[2])
child_num = int(args[3])

# 日付を分ける
year = d[:4]
month = d[4:6]
day = d[6:8]
dt = date(int(year),int(month),int(day))

# 日付の重複確認
# 日付だけ取り出す
datelist = session.query(Attend.entry_date).all() 
# 日付のタプルから要素を取り出す
list = []
for i in range(len(datelist)):
    list.append(datelist[i][0])
# 日付のリストに引数で入れた日付があるかを確認する
if (dt in list) == True:
    # seqだけどりだす
    seq_list = session.query(Attend.seq).filter_by(entry_date = dt).all()
    # seqのタプルから要素を取り出す
    list2 = []
    for i in range(len(seq_list)):
        list2.append(seq_list[i][0])
    # リストの末尾にある数値を取り出す
    seq_max = list2[-1] 
    # テーブルにデータ追加
    table = Attend(
    entry_date = dt,
    seq = seq_max + 1,
    adult = adult_num,
    child = child_num
    ) 
# 新規のデータ登録
else:
# テーブルにデータ追加
    table = Attend(
        entry_date = dt,
        seq = 1,
        adult = adult_num,
        child = child_num
    )

# INSERT処理
session.add(table)
# コミット
session.commit()