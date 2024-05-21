from database import session #１．データベースへの接続
from tables import Mst_hinmoku, Tbl_zaiko #２．テーブル定義
import sys
args = sys.argv

#---クラス定義
class Id:
    def __init__(self, id):    
        self.id = id        

class Hinmoku(Id):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

class Transaction(Id):
    def __init__(self, id, unit, unitprice, quantity, process):
        super().__init__(id)       
        self.unit = unit
        self.unitprice = unitprice        
        self.quantity = quantity
        self.process = process

class Operation:
    #品目マスタ登録メソッド
    def master_insert(self, hinmoku):
        check_mst = session.query(Mst_hinmoku).filter_by(id=hinmoku.id).first()
        #存在チェックし、存在しない場合は登録、存在する場合はFalseを返す
        if check_mst == None:
            insert_data = Mst_hinmoku(
                id = hinmoku.id,
                name = hinmoku.name,
            )
            session.add(insert_data)
            session.commit()
            return True
        else:
            return False
    #仕入売上メソッド
    def purchase_sales(self, transaction):
        update_stock = session.query(Tbl_zaiko).filter_by(id=transaction.id, unit=transaction.unit, unitprice=transaciton.unitprice).first()
        if update_stock == None:
            #売上で在庫がない場合はFalseを返す
            if transaction.process == "S":
                return False
            #仕入で在庫がない場合は登録
            insert_stock =Tbl_zaiko(
                id = transaction.id,
                unit = transaction.unit,
                unitprice = transaciton.unitprice,
                stock = transaction.quantity
            )
            session.add(insert_stock)
            session.commit()
        else:
            #仕入の場合（更新）
            if transaction.process == "P":
                update_stock.stock = update_stock.stock + transaction.quantity
            #売上の場合（更新）
            elif transaction.process == "S":
                #引数に設定した数量分、売上げることが出来る場合のみ売上を在庫から減算する
                if update_stock.stock - transaction.quantity < 0:
                    return False
                update_stock.stock = update_stock.stock - transaction.quantity
            session.add(update_stock)
            session.commit()
            return True
    #一覧出力メソッド        
    def show_list(self):
        #在庫データの取得（テーブル結合）
        stock_list = session.query(Mst_hinmoku, Mst_hinmoku.id, Mst_hinmoku.name, Tbl_zaiko.unit, Tbl_zaiko.unitprice, Tbl_zaiko.stock).join(Tbl_zaiko, Mst_hinmoku.id == Tbl_zaiko.id).order_by(Mst_hinmoku.id).all()
        #一覧出力
        for item in stock_list:
            if item.stock > 0:
                print("品目"+ item.id +"（"+ item.name +"）の在庫：" + str(item.stock) +item.unit + "（単価："+ str(item.unitprice) + "円）")

##---以後、メイン処理の記述
#インスタンスを生成
now_operation = Operation()
#引数を変数に代入（処理モード）
mode = args[1]
#品目マスタ登録（モード：1）
if mode == "1":
    hinmoku = Hinmoku(args[2], args[3])
    result = now_operation.master_insert(hinmoku)
    if result == True:        
        print("品目マスタに"+ hinmoku.id + "," +hinmoku.name + "を登録しました")
    elif result == False:
        print("品目マスタに"+ hinmoku.id + "は登録済みです")
#仕入登録（モード：2）
elif mode == "2":
    transaciton = Transaction(args[2], args[3], int(args[4]), int(args[5]), "P")
    result = now_operation.purchase_sales(transaciton)
    if result == True:    
        print("品目"+ transaciton.id + "（単価：" + str(transaciton.unitprice)+ "円）を"+ str(transaciton.quantity) + transaciton.unit + "仕入れました")    
#売上登録（モード：3）        
elif mode == "3":
    transaciton = Transaction(args[2], args[3], int(args[4]), int(args[5]), "S")
    result = now_operation.purchase_sales(transaciton)
    if result == True:
        print("品目"+ transaciton.id + "（単価：" + str(transaciton.unitprice)+ "円）を"+ str(transaciton.quantity) + transaciton.unit + "売上げました")
    elif result == False:
        print("売上数量に対して在庫が足りません。在庫を確認してください")
#在庫一覧出力（モード：4）    
elif mode == "4":
    now_operation.show_list()
