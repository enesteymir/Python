print("Haydi senin beden kitle endeksini ölçelim.")

kilo = int(input("Kilonuz: "))
boy = int(input("Boyunuz(cm): "))

endeks = kilo / ( (boy/100)**2 )

print("Beden Kitle Endeksiniz: {}".format(endeks))

if endeks < 18.5:
    print("Zayıfsınız...")
elif endeks >= 18.5 and endeks < 25:
    print("Normal Seviye")
elif endeks >= 25 and endeks < 30:
    print("Fazla Kilolarınız Var!")
elif endeks > 30:
    print("Obezsiniz. AZ YE!")
else:
    print("Bu ne olaki")