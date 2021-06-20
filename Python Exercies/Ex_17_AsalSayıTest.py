
def asalsayımı(num):

    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2,num):
            if num % x == 0:
                return False
        return True

while True:
    num = input("Bir sayı giriniz (Çıkmak için q ya basınız.) :")

    if (num == "q"):
        print("Çıkış yapılıyor")
        break
    else:
        num = int(num)
        if (asalsayımı(num)):
            print("{} bir asal sayıdır.".format(num))
        else:
            print("{} bir asal sayı değildir.".format(num))




