import sys
args = sys.argv

#引数を変数に代入
input1 = args[1] 
input2 = args[2]
input3 = args[3]

#数値の型に変換
num1 = int(input1)
num2 = int(input2)
num3 = int(input3)

#3つの合計を計算
output = num1 + num2 + num3

#計算結果の出力
print(output, end="")