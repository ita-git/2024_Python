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

#固定から可変に変更
#引数を変数に代入(リストに設定)
#numbers = (int(args[1]), int(args[2]), int(args[3]))
#for number in numbers:
#    calcvalue(number)

#引数をIdx：0を削除してidx：1以降の値で関数呼び出し
del args[0]
for i in args:
    calcvalue(int(i))