from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

# mysqlのDBの設定
DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "mysql"),
        "host": os.getenv("DB_HOST", "localhost"),
        "database":os.getenv("DB_DATABESE", "enshu")
    })

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True # True:実行のたびにSQLが出力
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# tables.pyで継承する
Base = declarative_base()
Base.query = session.query_property()