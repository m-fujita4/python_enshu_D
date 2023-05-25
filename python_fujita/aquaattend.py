import argparse
from datetime import date

import sqlalchemy
from database import session
from tables import AttendNum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help='', type=str)
    parser.add_argument('adult', help='', type=int)
    parser.add_argument('child', help='', type=int)
    args = parser.parse_args()

    year, month, day = args.date[0:4], args.date[4:6], args.date[6:8]
    today = date(int(year), int(month), int(day))

    hoge = session.query(sqlalchemy.func.count(AttendNum.seq)).filter_by(entry_date=today).all()

    seq = 1 + hoge[0][0]

    record = AttendNum(
        entry_date=today,
        seq=seq,
        adult=args.adult,
        child=args.child
    )

    session.add(record)
    session.commit()


if __name__ == '__main__':
    main()
