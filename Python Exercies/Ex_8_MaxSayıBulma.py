print("""
Merhaba. Bu uygulamamızda en büyük sayıyı bulacağız."
Lütfen 3 sayı giriniz. """)

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
c = int(input("Üçüncü sayıyı giriniz: "))

if a > b and a > c:
    print("En büyük sayımız: {}".format(a))
elif b > a and b > c:
    print("En büyük sayımız: {}".format(b))
elif c > a and c > b:
    print("En büyük sayımız: {}".format(c))
else:
    print("Heyy eşitlik var gibi")