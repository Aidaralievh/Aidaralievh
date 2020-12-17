print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


choice = input("Enter choice(1/2/3/4): ")



integero = '1234567890'
def check(num1, num2):
    if num1 and num2 not in integero or num1 not in integero or num2 not in integero:
        print('not int')
        breakpoint()
    if choice == '1':
        print(float(num1) + float(num2))
        breakpoint()
    elif choice == '2':
        print(float(num1) - float(num2))
        breakpoint()
    elif choice == '3':
        print(float(num1) * float(num2))
        breakpoint()
    elif choice == '4':
        print(float(num1) / float(num2))
        breakpoint()
    elif choice != '1' or '2' or '3' or '4':
        print('choice error')
        breakpoint()
    print('calculator done')

check(input(), input())