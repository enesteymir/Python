print("""
Vize Hesaplama Programına Hoşgeldiniz...
    """)

a = int(input("Vize1 Notunuzu Giriniz :"))
b = int(input("Vize2 Notunuzu Giriniz :"))
c = int(input("Final Notunuzu Giriniz :"))

totalnot = a*0.30 + b*0.30 + c*0.4

if totalnot >= 90:
    print("Helal reis puanın {} ve AA aldın.".format(totalnot))
elif totalnot >=85:
    print("Helal reis puanın {} ve BA aldın.".format(totalnot))
elif totalnot >=80:
    print("Helal reis puanın {} ve BB aldın.".format(totalnot))
elif totalnot >=75:
    print("Ooo reis puanın {} ve CB aldın.".format(totalnot))
elif totalnot >=70:
    print("Eh reis puanın {} ve CC aldın.".format(totalnot))
elif totalnot >=65:
    print("Hacı zar zor yırttın puanın {} ve DC aldın.".format(totalnot))
elif totalnot >=60:
    print("Hacı kaldın be:( puanın {} ve DD aldın.".format(totalnot))
elif totalnot >=55:
    print("Hacı nanay oldun insan az kasar da puanın {} ve FD aldın.".format(totalnot))
else:
    print("Hacı seneye artık puanın {} ve FF aldın.".format(totalnot))