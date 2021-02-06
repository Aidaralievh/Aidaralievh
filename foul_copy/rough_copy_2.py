def fibonacci(n):
    n = int(input('Enter the num: '))

    for i in range(n):
        for x in range(i):
            print(x, i)
