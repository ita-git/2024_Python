import sys
args = sys.argv

#引数を変数に代入
input_num = int(args[1])
#合計の変数にも引数を設定
sum_num = input_num

#100を超えるまで繰り返し（100の時だけbreak）
while sum_num <= 100:
    if sum_num == 100:
        out_text = "Just 100!"
        break
    sum_num = sum_num + input_num        
else:
    out_text = "Over!"

#結果の出力
print(out_text , end="")
