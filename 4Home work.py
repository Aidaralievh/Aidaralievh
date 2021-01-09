from random import randint

a=randint(0,9)
b=randint(0,9)
c=randint(0,9)
d=randint(0,9)
st0 = str(a) + str(b) + str(c) + str(d)



num = 0
while True:
    num += 1
    print("номер попытки: ", num)
    st = input("ведите число из 4х цифр:")
    if st == ("ответ"):
        print(st0)
        continue
    if len(st) != 4:
        print ("должно быть 4 цифры")
        continue
    Is=list(st)
    Is0 = list(st0)

    bulls = 0
    for j in range(4):
        if Is [j] == Is0[j]:
            bulls += 1
            Is[j] = ("")
            Is0[j] = ("*")

    if bulls == 4:
        print("вы угадали")
        break

    cows = 0
    for j in range(4):
        n = Is [j]
        for k in range(4):
            if n == Is0[k]:
                cows += 1
                Is0[k] = ("*")
                break

    print("быков: ", bulls)
    print("коров: ",cows)

