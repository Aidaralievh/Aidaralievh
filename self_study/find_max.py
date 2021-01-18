def find_max():
    a, b, c, d = map(int, input().split())
    sum_1 = a * b + c * d
    sum_2 = b * c + a * d
    sum_3 = d * b + a * c
    if sum_1 > sum_2:
        sum_all = sum_1
    else:
        sum_all = sum_2

    if sum_all < sum_3:
        sum_all = sum_3

    return sum_all


print(find_max())