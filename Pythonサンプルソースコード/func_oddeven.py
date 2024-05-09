import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

#引数を変数に代入(リストに設定)
numbers = (int(args[1]), int(args[2]), int(args[3]))
for number in numbers:
    calcvalue(number)
