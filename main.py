import random
ch = 1

answ = {}
min = 100000
max = 1
while ch < 101:
    a = random.randint(100,300)
    if a in answ:
        continue

    else:
        answ[ch] = a
        ch += 1

for i in answ.values():
    print(i)
    if min < i:
        continue
    else:
        min = i

    if  max > i:
        continue
    else:
        max = i
print(answ)
print(max)
print(min)
