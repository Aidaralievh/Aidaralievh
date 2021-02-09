i = open('input.txt')
o = open('output.txt', 'w')
n = i.read().split()  # [5,30,......]
arr = []
for i in n:
    arr.append(int(i))
num = arr[0]
summa = arr[1]
total_list = arr[2:(num + 2)]
total_list.sort()
counter = 0
new = 0
for i in total_list:
    counter += i
    if counter > summa:
        break
    new += 1
o.write(str(new))

a = [1, 45, 33, 22, 100, 50, 179, 129, 46, 55, 128, 200, 199, 200]  # -> 0,1000

for i in range(0, len(a) - 1):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)


