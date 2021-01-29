import random


class Monty:
    def __init__(self, choice, door):
        self.choice = choice
        self.door = door

    def choose_door(self):
        print('you did your choice')
        prize_door = random.randint(1, 3)
        if prize_door == 1 and self.choice == 1:
            revealed_door = 2
            print('revealed door: ', revealed_door)
        if prize_door == 2 and self.choice == 2:
            revealed_door = 3
            print('revealed door: ', revealed_door)
        if prize_door == 3 and self.choice == 3:
            revealed_door = 1
            print('revealed door: ', revealed_door)

        if prize_door == 1 and self.choice == 2:
            revealed_door = 3
            print('revealed door: ', revealed_door)
        if prize_door == 1 and self.choice == 3:
            revealed_door = 2
            print('revealed door: ', revealed_door)
        if prize_door == 2 and self.choice == 1:
            revealed_door = 3
            print('revealed door: ', revealed_door)
        if prize_door == 2 and self.choice == 3:
            revealed_door = 1
            print('revealed door: ', revealed_door)
        if prize_door == 3 and self.choice == 1:
            revealed_door = 2
            print('revealed door: ', revealed_door)
        if prize_door == 3 and self.choice == 2:
            revealed_door = 1
            print('revealed door: ', revealed_door)



        if self.choice == 1 and prize_door == 2:
            revealed_door = 3
            print('revealed door: ', revealed_door)
        if self.choice == 1 and prize_door == 3:
            revealed_door = 2
            print('revealed door: ', revealed_door)
        if self.choice == 2 and prize_door == 1:
            revealed_door = 3
            print('revealed door: ', revealed_door)
        if self.choice == 2 and prize_door == 3:
            revealed_door = 1
            print('revealed door: ', revealed_door)
        if self.choice == 3 and prize_door == 1:
            revealed_door = 2
            print('revealed door: ', revealed_door)
        if self.choice == 3 and prize_door == 2:
            revealed_door = 1
            print('revealed door: ', revealed_door)


        option = input('one of the door revealed, and it is not prize door, '
                       'do you want to change your mind: ')
        if option == 'n':
            print('your original choice was:', self.choice)
            if self.choice == prize_door:
                print('prize door:', prize_door)
                print('You win auto')
            if self.choice != prize_door:
                print('prize door:', prize_door)
                print('you loose, it is not prize door')
        if option == 'y':
            print('your original choice was:', self.choice)
            self.choice = int(input('choose the door: '))
            if self.choice == prize_door:
                print('prize door:', prize_door)
                print('your new choice:', self.choice)
                print('you win auto')
            else:
                print('your new choice:', self.choice)
                print('prize door:', prize_door)
                print('you loose, it is not prize door')


monty = Monty(int(input('choose the door: ')), [1, 2, 3])
monty.choose_door()