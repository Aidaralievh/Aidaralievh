inputt = open('input.txt')
output = open('output.txt', 'w')
read = inputt.read().split()
a = list(map(int, read))[1:]
h = []
for i in range(0, len(a), 3):
    time = a[i]*60*60 + a[i+1]*60 + a[i+2]
    h.append(time)

    for f in range(0, len(h) - 1):
        for j in range(0, len(h) - f - 1):
            if h[j] > h[j + 1]:
                h[j], h[j + 1] = h[j + 1], h[j]

for p in h:
    hour = (p % 86400) // 3600
    minutes = (p % 3600) // 60
    seconds = (p % 60)

    timme = f'{hour} {minutes} {seconds}\n'
    output.write(timme)




