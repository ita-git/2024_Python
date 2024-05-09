import sys
# コマンドライン引数のリストの取得
args = sys.argv   

#嫌いなものを変数に代入
dislike = args[1]

#エスケープシーケンスを使用して出力
print("I don\'t like \"" + dislike + "\"", end="")