from database import session    #１．データベースへの接続
from tables import Transport    #２．テーブル定義
import sys
args = sys.argv

# データを取得する
Translist=session.query(Transport).all()

#ファイルを開く
with open("C:\Seminar\python\output\\" + args[1] , mode="w", encoding="utf-8") as f:
#DBから取得したデータを書き込み    
    for linedata in Translist:
        #日付はYYYYMMDDに加工して出力する。""囲みと,区切りで出力。最後は改行あり
        f.write("\"" + str(linedata.date.strftime("%Y%m%d")) \
                + "\",\"" + str(linedata.seq) + "\",\"" + linedata.departure + "\",\"" + linedata.arrival \
                + "\",\"" +linedata.via +"\",\"" + str(linedata.amount) +"\"\n")