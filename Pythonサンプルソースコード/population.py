import sys
args = sys.argv

#引数を変数に代入(代入時点で整数型で代入)
rank = int(args[1]) 

#タプル worldlist の作成
nationlist = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Rossia", "Mexico")
#引数に設定した国名を出力
print(nationlist[rank - 1], end="")