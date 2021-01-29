

class Rectangle:
    def get_area(self):
        print('rectangele')


class Circle:
    def get_area(self):
        print('circle')


class Square:
    def get_area(self):
        print('square')


chores = [Rectangle(), Rectangle(), Circle(), Rectangle(), Square()]
for i in chores:
    i.get_area()