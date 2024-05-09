import qrcode
import sys
import os

args = sys.argv

#qrコードを作成するURL
img = qrcode.make(args[1])

#画像の保存（フルパスを作成して保存）
img.save(os.path.join("C:\Seminar\python\\files" , args[2]))