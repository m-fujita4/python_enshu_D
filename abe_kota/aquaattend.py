from datetime import date
from database import session
from attend_table import Attendnum
import sys

args = sys.argv
input_date=args[1]
adults=int(args[2])
children=int(args[3])

year=int(input_date[0:4])
month=int(input_date[4:6])
day=int(input_date[6:8])

#seq取り出し
seq_list=session.query(Attendnum.seq).filter_by(entry_date=date(year,month,day)).all()
#seq_list=session.query(Attendnum.seq).all()
#print(seq_list)
#print(seq_list[0],seq_list[1])

#seqリストが空の時
if not seq_list:
    attendnum=Attendnum(
    entry_date=date(year,month,day),
    seq=1,
    adult=adults,
    child=children
    )

#seqリストがすでに存在するとき
else:
    print(seq_list)
    seq_count=(max(seq_list)[0])
    print(seq_count)

    attendnum=Attendnum(
    entry_date=date(year,month,day),
    seq=seq_count+1,
    adult=adults,
    child=children
    )

"""
if seq_count > 1:
    new_seq=session.query(Attendnum).filter_by(seq=seq_count).first()
    new_seq.seq=seq_count+1
"""

    
"""
entry_date=session.query(Attendnum.entry_date).all()
print(entry_date)
seq=session.query(Attendnum.seq).all()
print(seq)
"""
"""
#entry_dateが既に存在するかチェック
for days in entry_date
if entry_date==date(year,month,day):

    attendnum=Attendnum(
    entry_date=date(year,month,day),
    seq=1,
    adult=adults,
    child=children
)   
"""


session.add(attendnum)
session.commit()

