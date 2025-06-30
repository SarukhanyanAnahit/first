class Mylist:
    def __init__(self, value):
        self.__value = []

    def __len__(self):
        return self.__value.__len__()

    def __getitem__(self, index):
        return self.__value.__getitem__(index)

    def __setitem__(self, index, item):
        self.__value.__setitem__(index, item)

    def append(self, item):
        self.__value = self.__value.__add__([item])

    def insert(self, index, item):
        left = self.__value[:index]
        right = self.__value[index:]
        self.__value = left.__add__([item]).__add__(right)

    def extend(self, elements):
        self.__value = self.__value.__add__(list(elements))

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return f"mylist({self.__value})"

ml = Mylist([4, 6])
ml.append(9)
ml.insert(5, 3)
ml.extend([10, 20, 30])

print(ml)
print(ml[4])
ml[2] = 99
print(ml)