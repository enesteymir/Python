print("""
**********************
Merhaba, Hesap Makinesi Programına Hoşgeldiniz.
Yapabildiğim işlemler;

1- Toplama İşlemi
2- Çıkarma İşlemi
3- Çarpma İşlemi
4- Bölme İşlemi

**********************
""")
a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))
islem = int(input("İşlem Numarasını Giriniz:"))
if islem == 1:
    print("İşlemin Sonucu: {}".format(a+b))
elif islem ==2:
    print("İşlemin Sonucu: {}".format(a-b))
elif islem ==3:
    print("İşlemin Sonucu: {}".format(a*b))
elif islem ==4:
    print("İşlemin Sonucu: {}".format(a/b))
else :
    print("Bende böyle bir işlem no yok ki :(")