from random import randint

a = []
for i in range(15):
    a.append(randint(1, 100))
a.sort()
print(a)


humanNum = int(input('Enter the number that you want to print: '))

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != humanNum and low <= high:
    if humanNum > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)