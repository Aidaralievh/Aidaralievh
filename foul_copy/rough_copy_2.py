class Sort:
    def __init__(self):
        self.list = [(10, 20, 30),
                     (7, 30, 00),
                     (23, 59, 59),
                     (13, 30, 30)]
        # self.pivot = self.list[6]
        # self.left = list(filter(lambda x: x < self.pivot, self.list))
        # self.center = [x for x in self.list if x == self.pivot]
        # self.right = []

    def bubble_sort(self):
        for j in range(len(self.list)):
            swapped = False
            i = 0
            while i < len(self.list) - 1:
                if self.list[i] > self.list[i + 1]:
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
                    swapped = True
                i = i + 1
            if not swapped:
                break
        print(self.list)

    # def quick_sort(self):
    #     if len(self.list) <= 1:
    #         return self.list
    #     for x in self.list:
    #         if x > self.pivot:
    #             self.right.append(x)
    #     return self.left + self.center + self.right


sort = Sort()
sort.bubble_sort()
# print(sort.quick_sort())
