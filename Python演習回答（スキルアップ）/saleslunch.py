import sys
args = sys.argv

#引数を変数に代入
torikara = int(args[1])
curry = int(args[2])

#売上高の計算
sales = torikara * 760 + curry * 850

print(sales, end="")