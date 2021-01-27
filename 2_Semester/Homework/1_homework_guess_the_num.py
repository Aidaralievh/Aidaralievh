from random import randint


class Guess_num:
    human_choice = -1
    comp_choice = -1

    def __init__(self):
        self.comp_choice = randint(1, 10)
        self.human_choice = int(input("Enter your num 0-10: "))
        print("comp_choice", self.comp_choice)
        print("human choice", self.human_choice)

    def win_or_lose(self):
        if self.human_choice == self.comp_choice:
            print("you win")
        elif self.comp_choice != self.human_choice:
            print("you lose")


game = Guess_num()
game.win_or_lose()
