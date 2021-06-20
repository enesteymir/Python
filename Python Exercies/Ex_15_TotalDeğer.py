print("""*******************
Gireceğiniz sayıları toplayacağım ve ne kadar etmiş bulacağız.
*******************""")

toplam = int(0)

while True:
    x = input("Haydi bir sayı gir! (Çıkmak istersen q' ya bas) : ")
    if x == "q":
        break
    toplam += int(x)

print("Toplam değerimiz {} 'dir.".format(toplam))

