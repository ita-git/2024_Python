from datetime import date
#import datetime    #モジュールごとのimportする記述
import sys
from database import session
from tables import Attendnum

#引数の取得
args = sys.argv

#引数を変数に代入
adult = int(args[2])
child = int(args[3])
#引数→日付の取得
dt = date(int(args[1][0:4]), int(args[1][4:6]), int(args[1][6:8]))

#連番最大値を取得
Attendget = session.query(Attendnum).filter_by(entry_date = dt).order_by(Attendnum.seq.desc()).first()

#取得できた場合は+1、それ以外の場合は1
if Attendget != None:
    seq = Attendget.seq + 1
else:
    seq = 1

#登録の値を設定
attendnum = Attendnum(
    entry_date = dt, 
    seq = seq, 
    adult = adult, 
    child = child
)

#INSERT
session.add(attendnum)

#コミット
session.commit()