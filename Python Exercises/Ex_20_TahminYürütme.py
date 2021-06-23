import random
import time

print("""
    Sayı Tahmin Etmece
    
    1 - 100 arası bir sayı tahmin edin ! 10 hakkınız var.
    """)

rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 5

while True:
    tahmin = int(input("Haydi tahmin et:"))

    if (tahmin<rastgele_sayı):
        print("Bakalım doğru mu ....")
        time.sleep(1)
        print("Daha yüksek bir sayı söylemelisin :(")
        tahmin_hakkı -= 1

    elif (tahmin>rastgele_sayı):
        print("Bakalım doğru mu ....")
        time.sleep(1)
        print("Daha düşük bir sayı söylemelisin :(")
        tahmin_hakkı -= 1

    else:
        print("Bakalım doğru mu ....")
        time.sleep(1)
        print("Helal be! Tutturdun.")
        break

    if (tahmin_hakkı==0) :
        print("Tahmin hakkınız bitti malesef.")
        break

