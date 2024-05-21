#商品名と金額の辞書型
goodslist = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ": 130}

#いちばん安い商品の金額を求める
pricelist = list(goodslist.values()) #辞書型のvalueのリスト化
pricelist.sort()                     #昇順並び替え
minimum = pricelist[0]               #先頭の要素が最低金額の為、要素0を取得

#商品名と金額の出力
for goodsname in goodslist.keys():
    print(goodsname + ":" + str(goodslist[goodsname]) + "円")

#投入金額のチェック（OKであればcheckflgがoffで後続処理へ）
checkflg = "X"
while checkflg == "X":
    input_money = int(input("投入金額を入力してください"))

    #10000円を超える金額かのチェック
    if input_money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        continue        

    #最低購入金額のチェック
    if input_money < minimum:
        print(str(input_money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        continue

    #1円玉、5円玉のチェック
    if not input_money % 10 == 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        continue
    #チェックでOKであれば、chekflgをoff
    checkflg = ""

#breakするまでループ
while True:
    buy = input("何を購入しますか（商品名/cancel）")
    #cancelの場合には、ループを抜ける
    if buy == "cancel":
        break
#######追加課題ここから######
    #リストにない商品が入力された場合
    check_key = buy in goodslist.keys()
    if check_key == False:
        print("入力した商品が存在しません。一覧出力された商品から選択して入力してください")
        continue
#######追加課題ここまで######

#商品購入の計算    
    input_money = input_money - goodslist[buy]
    #最低金額の商品を残金が下回った場合にはループを抜ける
    if input_money < minimum:
        break

    #続けて購入できる残金が残っている場合
    print("残金：" + str(input_money) + "円")
    nextbuy = input("続けて購入しますか（Y/N）")

    #続けて購入する場合
    if nextbuy == "Y":
    #商品名と金額の出力
        for goodsname in goodslist.keys():
            print(goodsname + ":" + str(goodslist[goodsname]) + "円")        
        continue
    #購入をやめる場合ループを抜ける    
    elif nextbuy == "N":
        break

#おつりの出力
moneylist = {10000:"札", 5000:"札", 2000:"札", 1000:"札", 500:"玉", 100:"玉", 50:"玉", 10:"玉"}

if input_money > 0:
    print("おつり")

    #大きい金種から順に割り当てるループ
    for money in moneylist.keys():
        #割り当てる金種が残金よりも大きい場合には次の金種へ
        if money > input_money:
            continue
        #おつり金額の出力    
        print(str(money)+ "円" + moneylist[money] + "：" + str(input_money // money)+ "枚")
        input_money = input_money - (money * ( input_money // money))     