print("Girilen kenarlara göre hangi geometri tipi olduğunu keşfedelim.")

tip = int(input("Üçgen tipi ise 1'i , Diktörtgen tipi ise 2 değerini girin : "))

if tip == 2:
    a = int(input("İlk kenarın uzunluğunu girin: "))
    b = int(input("İkinci kenarın uzunluğunu girin: "))
    c = int(input("Üçüncü kenarın uzunluğunu girin: "))
    d = int(input("Dördüncü kenarın uzunluğunu girin: "))

    if a == b == c == d:
        print("Bu bir kare!")
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        print("Bu bir dikdörtgen!")
    else:
        print("Bu normal bir dörtgen.")

elif tip == 1:
     x = int(input("İlk kenarın uzunluğunu girin: "))
     y = int(input("İkinci kenarın uzunluğunu girin: "))
     z = int(input("Üçüncü kenarın uzunluğunu girin: "))

     if (abs(x + y) > z and abs(x + z) > y and abs(y + z) > x):
        if x == y == z:
            print("Bu bir eşkenar üçgen!")
        elif (x == y) or (x == z) or (y == z):
            print("Bu bir ikizkenar üçgen!")
        else:
            print("Bu bir sıradan üçgen.")
     else:
         print("Bu bir üçgen değil.")

else:
    print("Ben de bu tip yok ki")
