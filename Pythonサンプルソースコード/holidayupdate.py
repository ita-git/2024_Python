from datetime import date
from database import session
from tables import Holiday

# 更新するデータの取得
holiday = session.query(Holiday).filter_by(holi_date=date(2023, 1, 1)).first()
# 更新するデータの更新
holiday.holi_text = "元旦"

#UPDATE処理
session.add(holiday)
#コミット
session.commit()
