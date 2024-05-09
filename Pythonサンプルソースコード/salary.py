import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#引数を変数に代入
salary = int(args[1])

#税額計算のため、給与1,000,000での判定
if (salary > 1000000):
    tax = (salary - 1000000) * 0.2 + 100000
else:
    tax = salary * 0.1

tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
#支給額 = 給与 - 税額
pay = salary - tax

#支給額の出力
print("支給額:"+ str(pay) + "、税額:" + str(tax), end="")
