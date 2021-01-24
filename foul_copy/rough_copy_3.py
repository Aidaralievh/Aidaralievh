class Student:
    def __init__(self, born, countr):
        self.born = born
        self.countr = countr

    def get_data(self):
        print(self.born, self.countr)


obj1 = Student("bish", "russ")
obj1.get_data()
obj2 = Student("osh", "usa")
obj2.get_data()


comp_guess = randint(0, 11)

        print(comp_guess)
        human_guess = int(input("Please enter your num 0-10: "))
        if comp_guess == human_guess:
            print("you guessed")
        elif comp_guess != human_guess:
            print("you didn't guessed"