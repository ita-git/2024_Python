import sys
from introfamily import IntroFam
args = sys.argv

#インスタンスの生成
outtext = IntroFam(args[1], args[2], args[3])

#名前行、年齢行、飼い猫の名前と出力
print(outtext.name_out()) #名前の出力
print(outtext.age_out())  #年齢の出力
print(outtext.cat_out())  #飼い猫の出力
