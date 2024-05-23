import qrcode
import sys
import os

args = sys.argv
i = 1

with open (args[1], encoding="utf-8") as a_file:
    for file in a_file:
#qrコードを作成するURL
        img = qrcode.make(file)
#画像の保存（フルパスを作成して保存）
        img.save(os.path.join("C:\Seminar\python\output" , str(i)+".png"))
        i = i + 1

