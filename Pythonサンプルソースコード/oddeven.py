import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])

#あまりを算出
mod = num % 2

#あまりの値から奇数偶数判定
if mod != 0:
    print("奇数", end="")
else:
    print("偶数", end="")