print("""
************************
Mükemmel Sayı Kontrol Programına Hoşgeldiniz..
************************
""")

sayı = int(input("Bir sayı giriniz:"))

böl = range(1,sayı)
bölmüş =[]
bölen = 0

for x in böl:
    if sayı % x == 0:
       bölen += x
       bölmüş.append(x)

print("Kalansız bölen sayılar şunlar : {} ".format(bölmüş))
if bölen == sayı:
    print("Tebrikler! Bu bir mükemmel sayı")
else:
    print("Maalesef :( Bu bir mükemmel sayı değilmiş.")