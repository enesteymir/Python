print("Kök bulma programına hoşgeldiniz. Lütfen denklemden gerekli değerleri giriniz.")

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

delta = b**2 - 4*a*c

if delta>0:

    x1= (-b - delta**0.5) / (2*a)
    x2= (-b + delta**0.5) / (2*a)
    print("Birinci Kök: {}\nİkinci Kök: {}".format(x1,x2))

else :
    print("Gerçek sayılı kök yok")

