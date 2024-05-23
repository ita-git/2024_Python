from datetime import date
from database import session
from tables import Transport
import sys
args = sys.argv

#登録に失敗した場合には、except以下を処理（例外処理）
try:    
# 登録するデータの編集
    insdata = Transport(
        date = date(int(args[1][0:4]), int(args[1][4:6]), int(args[1][6:8])),
        seq = int(args[2]),
        departure = args[3],
        arrival = args[4],
        via = args[5],
        amount = int(args[6])
    )

    #INSERT処理
    session.add(insdata)
    #コミット
    session.commit()
    print("交通費精算テーブルにデータを登録しました", end="")
except:
    #ロールバック（1行データのため、不要だが念のため（お作法））
    session.rollback()
    print("error:交通費精算テーブルにデータを登録できませんでした", end="")

