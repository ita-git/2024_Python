from database import session
from tables import Stations
import sys
args = sys.argv

#引数を変数に代入
input_from = args[1] 
input_to = args[2]

# データを取得する
stations=session.query(Stations).filter(Stations.name.in_([input_from, input_to])).all()

#絶対値
sta_dis = abs(stations[0].kilo - stations[1].kilo)

#出力（小数第二位まで出力）
print("{:.2f}".format(sta_dis), end="")

