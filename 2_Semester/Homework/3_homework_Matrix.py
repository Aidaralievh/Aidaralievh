class Matrix:
    def __init__(self):
        self.a, self.b = map(int, input('Enter a numbers: ').split())

    def get_matrix(self):
        counter = 0
        for i in range(self.a):
            for j in range(self.b):                print(counter % 10, end=' ')
                counter += 1
                print()


matrix = Matrix()
matrix.get_matrix()

