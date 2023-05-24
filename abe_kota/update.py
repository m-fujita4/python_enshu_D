from datetime import date
from database import session
from table import Holiday

#更新データの取得
holiday=session.query(Holiday).filter_by(holi_date=date(2024,1,1)).first()

#更新するデータの更新
holiday.holi_text="元旦"

session.add(holiday)
session.commit()