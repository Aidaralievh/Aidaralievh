
N = 10
a = [
        10, 20, 30,
        7, 30, 00,
        23, 59, 59,
        13, 30, 30]

for j in range(N-1):
    if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]

print(a)