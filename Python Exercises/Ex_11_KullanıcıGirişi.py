print(""" 
 ************************** 
      Kullanıcı Girişi Programına Hoşgeldiniz.
 **************************  
      """)

kullanıcı_adı = "enstymr"
parola = int(6233)

hak = 3

while True:
    giris_ad = input("Lütfen Kullanıcı Adınızı Giriniz:")
    giris_parola=int(input("Lütfen Parolayı Giriniz:"))

    if ((giris_ad!=kullanıcı_adı) and (giris_parola==parola)):
        print("Kullanıcı adını yanlış girdiniz...")
        hak -= 1
    elif ((giris_ad==kullanıcı_adı) and (giris_parola!=parola)):
        print("Şifreyi yanlış girdiniz...")
        hak -= 1
    else:
        print("Tebrikler! Başarılı giriş.")
        break
    if hak == 0:
        print("Hakkın bitti reis.")
        break