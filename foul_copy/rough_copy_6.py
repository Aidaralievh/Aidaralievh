from random import *

n = randint(1, 3)
list_door = [1, 2, 3]

list_door.remove(n)
print(n)
print(list_door)

leading = choice(list_door)
print(leading)
list_door.remove(leading)
list_door.append(n)
print(list_door)

human = int(input("Введите число: "))
if leading == n:
    print("ты выйграл машину")
else:
    print("ты проиграл")