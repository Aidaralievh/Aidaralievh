# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
#
#
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

diff21 = 21
n = int(input("введите число"))

if n > diff21:
    n -= diff21
    n *= 2
    print(n)


elif diff21 >= n:
    diff21 -= n
    print(diff21)
