a = [1, 45, 33, 22, 100, 50, 179, 129, 46, 55, 128, 200, 199, 200]  # -> 0,1000

for i in range(0, len(a) - 1):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)