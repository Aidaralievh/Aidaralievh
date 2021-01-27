from random import *


class Choice_of_doors:

    def __init__(self, first_door, second_door, third_door, human_choice, comp_choice, leading_choice):
        self.first_door = first_door
        self.second_door = second_door
        self.third_door = third_door
        self.human_choice = human_choice
        self.comp_choice = comp_choice
        self.leading_choice = leading_choice

    def main(self):
        print("Firts door = 1  "  "Second door = 2  "  "third door = 3  ")
        self.comp_choice = randint(1, 3)
        self.doors = [1, 2, 3]
        self.human_choice = int(input("Enter your doors 1-3: "))
        self.doors.remove(self.comp_choice)
        self.doors.remove(self.human_choice)


        self.leading = choice(self.doors)

        self.doors.remove(self.leading)
        self.doors.append(self.comp_choice)

        print("comp_choice,", self.comp_choice)
        print("human_choice", self.human_choice)
        print("leading choice", self.leading)


door = Choice_of_doors()
