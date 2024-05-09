import sys
args = sys.argv

#引数に設定した回数を整数型の変数に代入
count_sheep = int(args[1])

#引数の回数分繰り返し(endの引数は設定せず、デフォルト改行コードあり)
for count_up in range(count_sheep):
    print ("ひつじが"+ str(count_up+1) + "匹")