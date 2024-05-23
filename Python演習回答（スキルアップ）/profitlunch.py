import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#引数を変数に代入
torikara = int(args[1])
curry = int(args[2])

#売上高の計算
sales_torikara = torikara * 760 
sales_curry = curry * 850
sales = sales_torikara + sales_curry

#原価の計算
cost_torikara = Decimal(str(sales_torikara * 0.323 )).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
cost_curry = Decimal(str(sales_curry * 0.284 )).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
cost = cost_torikara + cost_curry

#粗利の計算
profit_torikara = sales_torikara - cost_torikara
profit_curry = sales_curry - cost_curry
profit = profit_torikara + profit_curry

print("売上高："+ str(sales) + "、原価：" + str(cost) + "、粗利：" + str(profit) , end="")