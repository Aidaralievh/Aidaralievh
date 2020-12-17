def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b
def give_string(a, b):
    return a, b
print("Enter 1 for addition: ")
print("Enter 2 for subtraction: ")
print("Enter 3 for multiplication: ")
print("Enter 4 for division: ")
print('Enter 5 for return string: ')

operation = input(' ')

number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")

if operation == "1":
    print(number_1 + "+" + number_2 + "=" + add(number_1, number_2))

if operation == "2":
    print(number_1 + "-" + number_2 + "=" + subtract(number_1, number_2))

if operation == "3":
    print(number_1) + "*" + number_2 + "=" + multiply(number_1, number_2)

if operation == "4":
    print(number_1 + "/" + number_2 + "=" + divide(number_1, number_2))
if operation == '5':
    print(give_string(number_1, number_2))


