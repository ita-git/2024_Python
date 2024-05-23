namelist = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

number = len(namelist)  #要素数をカウント

number = number - 1     #添え字は0からのため1マイナス

while number >= 0:      #大きい添え字の要素から削除
    del namelist[number]
    number = number -2

print(namelist, end="")