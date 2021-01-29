class Person:
    def __init__(self):
        print('breathe')


class Robot:
    def __init__(self):
        print('kill')


class PoliceMan:
    def __init__(self):
        print('arrest')


class RoboCop(PoliceMan, Robot, Person):
    pass



c = RoboCop()
print(c)