import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
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
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)    
    child = Column('child', Integer) 

#テーブル：Stationsの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))    
    kilo = Column('kilo', Numeric(6,2)) 

#テーブル：Transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20))    
    arrival = Column('arrival', String(20))    
    via = Column('via', String(40))    
    amount = Column('amount', Integer) 

#テーブル：Mst_merchandiseの定義
class Mst_merchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)    

#テーブル：Tbl_stockの定義
class Tbl_stock(Base):
    __tablename__ = 'tbl_stock'
    id = Column('id', String(10), primary_key = True)
    stock = Column('stock', Integer) 

#テーブル：Tbl_moneyの定義
class Tbl_money(Base):
    __tablename__ = 'tbl_money'
    price = Column('price', Integer, primary_key = True)
    number = Column('number', Integer)    

#テーブル：Tbl_messageの定義
class Tbl_message(Base):
    __tablename__ = 'tbl_message'
    seq = Column('seq', Integer, primary_key = True, autoincrement=True)
    message = Column('message', String(100))
    datetime = Column('datetime', DateTime)  

#テーブル：Mst_hinmokuの定義
class Mst_hinmoku(Base):
    __tablename__ = 'mst_hinmoku'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))

#テーブル：Tbl_zaikoの定義
class Tbl_zaiko(Base):
    __tablename__ = 'tbl_zaiko'
    id = Column('id', String(10), primary_key = True)
    unit = Column('unit', String(10), primary_key = True)   
    unitprice = Column('unitprice', Integer, primary_key = True)          
    stock = Column('stock', Integer)        

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)