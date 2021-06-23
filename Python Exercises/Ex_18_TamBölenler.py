def tambolenler(num):
    tambolenlerlist = []

    for i in range(2,num+1):
        if num % i == 0:
            tambolenlerlist.append(i)
    return tambolenlerlist


while True:
    num = input("Bir sayı giriniz. [Çıkmak için q ' ya basınız.] :")

    if num == 'q':
        print("Çıkış Yapılıyor...")
        break
    else:
        num = int(num)
        print("Tam bölenlerin listesi {}:".format(tambolenler(num)))

