import random


class Game:

    your_choice = -1
    comp_choice = -1

    def __init__(self):
        self.your_choice = int(input('enter number:[0,1,2]'))
        print('your choiceis', self.your_choice)
        self.comp_choice = random.randint(0, 3)
        print('comp_choice is', self.comp_choice)

    def get_winner(self):
        if self.your_choice == self.comp_choice:
            print('You Draw')
        elif self.your_choice == 0 and self.comp_choice == 1:
            print('You Draw')
        elif self.your_choice == 0 and self.comp_choice == 2:
            print('You Loser')
        elif self.comp_choice == 0 and self.your_choice == 1:
            print('You Loser')
        elif self.comp_choice == 0 and self.your_choice == 2:
            print('You Loser')
        pass


game = Game()
game.get_winner()
