import datetime
from database import session #１．データベースへの接続
from tables import Mst_merchandise, Tbl_stock, Tbl_money, Tbl_message   #２．テーブル定義

#更新後に何度でも呼び出せるように商品、在庫データの取得,一覧出力を関数にしておく
def getlist():
    pricelist = []
    #データを取得する
    merchlist=session.query(Mst_merchandise, Mst_merchandise.id, Mst_merchandise.name, Mst_merchandise.price,Tbl_stock.stock).join(Tbl_stock, Mst_merchandise.id == Tbl_stock.id).all()

    #商品一覧の出力
    for merchandise in merchlist:
        if merchandise.stock > 0:
            print(merchandise.name + "：" + str(merchandise.price) + "円")
            pricelist.append(merchandise.price)
    #戻り値
    return merchlist, pricelist

#起動時用の商品在庫データの取得、一覧出力
merchlist, pricelist = getlist()

#いちばん安い商品の金額を求める
pricelist.sort()                     #昇順並び替え
minimum = pricelist[0]               #先頭の要素が最低金額の為、要素0を取得

#投入金額のチェック（OKであればcheckflgがoffで後続処理へ）
checkflg = "X"
while checkflg == "X":
    input_money = int(input("投入金額を入力してください"))
    copy_input = input_money
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
    check_key = "X"
    for merchandise in merchlist:
        if merchandise.name == buy:
            check_key = ""
            break

    if check_key == "X":
        print("入力した商品が存在しません。一覧出力された商品から選択して入力してください")
        continue
#######追加課題ここまで######

#商品購入の計算    
    for merchandise in merchlist:
        if merchandise.name == buy:
            input_money = input_money - merchandise.price
            update_stock = session.query(Tbl_stock).filter_by(id=merchandise.id).first()
            update_stock.stock = update_stock.stock - 1
            session.add(update_stock)
            session.commit()
            break
        
    #最低金額の商品を残金が下回った場合にはループを抜ける
    if input_money < minimum:
        break

    #続けて購入できる残金が残っている場合
    print("残金：" + str(input_money) + "円")
    nextbuy = input("続けて購入しますか（Y/N）")

    #続けて購入する場合
    if nextbuy == "Y":
        #商品名と金額の取得と一覧出力
        merchlist, pricelist = getlist()
        continue
    #購入をやめる場合ループを抜ける    
    elif nextbuy == "N":
        break    

#おつりの出力
moneylist = {10000:"札", 5000:"札", 2000:"札", 1000:"札", 500:"玉", 100:"玉", 50:"玉", 10:"玉"}

#大きい金種から順に割り当てるループ（投入金額加算用）
for money in moneylist.keys():
    #割り当てる金種が残金よりも大きい場合には次の金種へ
    if money > copy_input:
        continue
    #加算する貨幣の枚数の計算
    plus_count = copy_input // money
    rec_money=session.query(Tbl_money).filter_by(price=money).first()
    rec_money.number = rec_money.number + plus_count
    #貨幣テーブルの更新     
    session.add(rec_money)
    session.commit()
    #加算した後の残の計算   
    copy_input = copy_input - (money * ( copy_input // money))     

#大きい金種から順に割り当てるループ（おつり減算用）
print("おつり")
for money in moneylist.keys():
    #割り当てる金種が残金よりも大きい場合には次の金種へ
    if money > input_money:
        continue
    #減算する貨幣の枚数の計算
    minus_count = input_money // money
    rec_money=session.query(Tbl_money).filter_by(price=money).first()
    rec_money.number = rec_money.number - minus_count 
    if rec_money.number <= 10:
        message = Tbl_message(
            message = str(money) + "円の残枚数が" + str(rec_money.number) + "枚になりました。確認してください",
            datetime = datetime.datetime.now()
        )
        session.add(message)
        session.commit()
    #貨幣テーブルの更新    
    session.add(rec_money)
    session.commit() 
    #おつり金額の出力    
    print(str(money)+ "円" + moneylist[money] + "：" + str(input_money // money)+ "枚")
    input_money = input_money - (money * ( input_money // money))         