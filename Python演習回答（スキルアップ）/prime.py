import sys
args = sys.argv

#引数を変数に代入
number = int(args[1]) #チェック対象
div = number // 2     #チェック対象の半分（整数）
cnt = 2               #割る数(2以上で割る)
flg_not = ""          #チェック用フラグ

if number < 1000:
    while cnt <= div:
        check = number % cnt
        if check == 0:
            flg_not = "X"
            break
        cnt = cnt + 1

    if flg_not == "X":
        print("not")
    else:
        print("prime")

else:
    print("1000以上は判定できません")
