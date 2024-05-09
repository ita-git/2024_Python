import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Holiday(Base):
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key = True)
    holi_text = Column('holi_text', String(20))

#テーブル：Attendnumの定義
class Attendnum(Base):
    __tablename__ = 'attendnum'
    date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)    
    child = Column('child', Integer) 

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)