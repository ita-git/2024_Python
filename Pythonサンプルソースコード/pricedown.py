import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]       #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")     #果物類をタプルで定義
alcohol = ("ビール", "日本酒")              #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#果物類の価格変更
if hm_class == "果物類":
    for fr in fruits:
        price = hinmoku[fr] - price_down
        if price < 1:
            price = 1                
        hinmoku[fr] = price
#酒類の価格変更        
if hm_class == "酒類":
    for al in alcohol:
        price = hinmoku[al] - price_down
        if price < 1:
            price = 1                
        hinmoku[al] = price
#麺類の価格変更        
if hm_class == "麺類":
    for nd in noodles:
        price = hinmoku[nd] - price_down
        if price < 1:
            price = 1                
        hinmoku[nd] = price

print(hinmoku, end="")