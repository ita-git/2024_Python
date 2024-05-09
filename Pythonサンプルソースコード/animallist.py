import sys
args = sys.argv

#引数を変数に代入
place = int(args[1]) 
name = args[2]

#リスト anilmals の作成
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#引数の要素数の位置に、挿入
animals.insert(place, name)
#最後の要素を削除
length = len(animals)
del animals[length - 1]
#ソート
animals.sort()

#リスト全体を出力
print(animals, end="")