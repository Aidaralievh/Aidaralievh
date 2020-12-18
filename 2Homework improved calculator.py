print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")


def check(num1, num2):
    if num1.isnumeric() == False or num2.isnumeric() == False:
        print('not int')
        return
    if choice == '1' and num1.isnumeric() and num2.isnumeric():
        print(float(num1) + float(num2))
    elif choice == '2' and num1.isnumeric() and num2.isnumeric():
        print(float(num1) - float(num2))
    elif choice == '3' and num1.isnumeric() and num2.isnumeric():
        print(float(num1) * float(num2))
    elif choice == '4' and num1.isnumeric() and num2.isnumeric():
        print(float(num1) / float(num2))
    elif choice != '1' or '2' or '3' or '4':
        print('choice error')
    print('calculator done')


check(input(), input())
