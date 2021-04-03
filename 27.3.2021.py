

def num (data):
    ch = 0
    answ1 = 0
    for i in data:
        ch += 1
        answ1 += int(i)
    answ = answ1**ch
    if int(data) > answ:
        print(True)
    elif int(data) < answ:
        print(False)
    else:
        print(None)


num('1234')
