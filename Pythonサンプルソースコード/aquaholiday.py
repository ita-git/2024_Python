from datetime import date
#import datetime    #モジュールごとのimportする記述
import sys
#mysqlDB接続、テーブル
from database import session
from tables import Holiday

args = sys.argv

#引数を変数に代入
input_date = args[1]
adult = int(args[2])
child = int(args[3])

#曜日の取得
dt = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
#dt = datetime.date(int(i_date[0:4]), int(i_date[4:6]), int(i_date[6:8]))　#from無しの場合の記述方法

#土日は、大人2,400円、子供1,500円
if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun" :
    pay = 2400 * adult + 1500 * child
#平日は、大人2,000円、子供1,200円
else:
    get_date = session.query(Holiday.holi_date).filter_by(holi_date = dt).first()
    if get_date is None:
        pay = 2000 * adult + 1200 * child  
    else:      
        pay = 2400 * adult + 1500 * child

#合計金額の出力
print(pay, end="")
