import sys
args = sys.argv

# 引数から変数に各教科の点数を代入
sc_math = int(args[1])
sc_japanese = int(args[2])
sc_english = int(args[3])

#全教科70点以上か判定（OKならその時点で合格）
if (sc_math >= 70 and sc_japanese >= 70 and sc_english >= 70):
    print("合格", end="")
else:
    if (sc_math + sc_japanese + sc_english >= 220):           #全教科合計画220点以上か判定
        if (sc_math >= 50 and sc_japanese >= 50 and sc_english >= 50):    #各教科50点以上か判定
            print("合格", end="")  
        else:
            print("不合格", end="")
    else:
        print("不合格", end="")
          