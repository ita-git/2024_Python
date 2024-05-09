import sys
args = sys.argv

#引数を変数に代入
input_from = args[1] 
input_to = args[2]

#駅名と東京駅からの距離を辞書型にセット
stations = { "東京":0 , "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35 }

#のぞみ停車駅以外を入力した場合の例外処理
try:
#引数の駅の東京からの距離を取得
    dis_from = stations[input_from]      
    dis_to = stations[input_to]          
#駅間の計算
    sta_dis = dis_to - dis_from
#絶対値で計算
    sta_dis = abs(sta_dis)
#出力（小数第一位まで出力）
    print("{:.2f}".format(sta_dis), end="")
except:
    print("のぞみの停車駅を引数に設定してください")
