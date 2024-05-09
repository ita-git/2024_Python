import sys
args = sys.argv

#引数を変数に代入
in_text = args[1] 
place = int(args[2])

#文字列の分割
split_text = in_text.split()

#出力
print(split_text[place - 1], end="")