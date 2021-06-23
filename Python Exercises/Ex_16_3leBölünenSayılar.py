# 1.YOL
sayılar = range(1,101)
bölünenler = []

for x in sayılar:
    if x % 3 == 0:
        bölünenler.append(x)
print(bölünenler)



# 2.YOL
sayılar = range(1,101)
for i in sayılar:
    if (i % 3 != 0):
        continue
    print(i)



# 3.YOL
liste = [x for x in range(1,101) if x % 3 == 0]
print(liste)