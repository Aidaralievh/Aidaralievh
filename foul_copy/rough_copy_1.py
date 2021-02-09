
num1 = input('enter the 1 num: ').split(' ')
num2 = input('enter the 2 num: ').split(' ')
num3 = input('enter the 3 num: ').split(' ')
num4 = input('enter the 4 num: ').split(' ')

a = [num1, num2, num3, num4]

for i in range(0, len(a) - 1):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)