import sys
from decimal import Decimal, ROUND_UP
args = sys.argv

#引数を変数に代入
dis = int(args[1])

#初乗り運賃
price = 630

#1500円以上の場合の計算
if dis > 1500:
    #98円をかける回数を切り上げて算出
    add = Decimal(str((dis - 1500) / 344)).quantize(Decimal("0"), rounding=ROUND_UP)
    price = price + (add * 98)

#出力
print(price, end="")