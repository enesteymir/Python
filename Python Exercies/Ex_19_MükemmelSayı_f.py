
def mukemmel(num):
    toplam = 0

    for i in range(1,num):
        if num % i == 0:
            toplam += i
    return toplam == num

mükemmels = []
for i in range(1,1001):
    if mukemmel(i):
       mükemmels.append(i)
print("Mükemmel Sayılar :{} ".format(mükemmels))