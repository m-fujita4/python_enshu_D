import sys
from sqlalchemy import Column,Integer,Date
from database import Base
from database import ENGINE

class Attendnum(Base):
    __tablename__='attendnum'
    entry_date=Column('entry_date',Date,primary_key=True)
    seq=Column("seq",Integer,primary_key=True)
    adult=Column("adult",Integer)
    child=Column("child",Integer)

def main(args):

    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)
    