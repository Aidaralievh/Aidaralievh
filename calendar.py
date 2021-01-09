def calculator(num1, num2, operation):
    if num1 != '':
        if operation != '':
            if num2 != '':
                if operation == "+":
                    return num1 + num2
                elif operation == "-":
                    return num1 - num2
                elif operation == "/":
                    return num1 / num2
                elif operation == "*":
                    return num1 * num2
                else:
                    return "Введите одну из предложеных операций!!"
            else:
                return "Введите второе число!"
        else:
            return "Введите операцию!"
    else:
        return "Введите первое число!"


try:
    n1 = int(input("Введите первое число"))
    op = input("Введите математический знак:\n + для сложения чисел,"
               "\n  - для вычитания чисел, \n / для деления чисел, \n * для умножения чисел")
    n2 = int((input("Введите второе число")))
    print(type(n1), type(n2))
except:
    n1 = int(input("ВВедите число а не строку!!!"))
    op = input("Введите математический знак:\n + для сложения чисел,"
               "\n  - для вычитания чисел, \n / для деления чисел, \n * для умножения чисел")
    n2 = int(input("ВВедите число а не строку!!!!"))
    print(type(n2), type(n1))
