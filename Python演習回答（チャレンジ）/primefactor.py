import sys
args = sys.argv

#引数を変数に代入
number = int(args[1]) #チェック対象
output =  []          #出力用リスト
prime_check = 2       #素数チェック用(2から順に整数が素数かチェックする)

#引数に設定された値を1になるまで割り込む
while number > 1:
    flg_not = ""      #素数判定用フラグ 
      
# 2から順に整数が素数か判定を行う    
    cnt = 2           #1ではすべて割り切れるため2以上で割ることが出来る数字が自分自身のみかチェック
    prime_div = prime_check // 2   #2で割った数の商を求める。2で割った商までを判定すれば素数か判定できるため
    while cnt <= prime_div:        #2から素数か否かを判定する数の2で割った商まで繰り返し処理
        check = prime_check % cnt  #素数チェック用の変数を2から順に割ったあまりを算出する
        if check == 0:             #あまりが0の場合は素数以外（次行でフラグON）
            flg_not = "X"
            break
        cnt = cnt + 1

# 素数の場合のみ、チェック対象を割ることが出来るか確認 （フラグOFFの場合のみ元の整数を割る）
    if not flg_not == "X":

        up_check = 0
        while up_check == 0:       #同じ素数で複数回分解できる可能性があるため、あまりが0の間割り続ける
            up_check = number % prime_check
            if up_check == 0:
                number = number // prime_check  #元の数を割る
                output.append(prime_check)      #結果用リストに格納する
            else:
                break

    prime_check = prime_check + 1  #次の整数が素数かどうかの判定から繰り返すために+1をする

#結果出力
print(output, end="")

