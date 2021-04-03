
data = input(':')
slova = data.split(' ')
answ = {}
for i in slova:
    if i in answ:
        for y in answ.values():
            ff = int(y)
            ff += 1
            answ[i] = ff
            ff = 0
    else:
        answ[i] = 1
print(answ)


