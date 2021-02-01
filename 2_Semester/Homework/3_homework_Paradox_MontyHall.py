import random


class MontyHall:

    def __init__(self):
        self.change_door = int(input('Do you want to change the door: [0,1]'))
        self.user_choice = int(input('Enter a number: '))
        self.comp_choice = random.randint(0, 2)
        self.opened_doors = [0, 0, 0]
        self.prized_doors = [0, 0, 0]

    def main(self):
        self.prized_doors[self.comp_choice] = 1
        self.opened_doors[self.user_choice] = 1
        doors = []
        for i in range(3):
            if self.opened_doors[i] == 0 and self.prized_doors[i] == 0:
                doors.append(i)
        opened_door = random.choice(doors)
        self.opened_doors[opened_door] = -1
        self.prized_doors[opened_door] = -1
        print('your choice', self.opened_doors)
        print('comp choice', self.prized_doors)
        is_winner = -1

        if self.change_door == 1:
            for i in range(3):
                if self.opened_doors[i] == 0:
                    is_winner = (self.prized_doors[i])
                    break
        if self.change_door == 0:
            is_winner = (self.prized_doors[self.user_choice])
        if is_winner:
            print('you win')
        else:
            print('you loose')


montyhall = MontyHall()
montyhall.main()