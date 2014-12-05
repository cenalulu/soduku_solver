__author__ = 'michellezhou'


class SodukuTable():
    def __init__(self):
        self.__table = list()
        for x in range(0, 8):
            row = list()
            for y in range(0, 8):
                row.append(0)
            self.__table.append(row)

    def get_v(self, x, y):
        return self.__table[x][y]

    def set_v(self, x, y, v):
        self.__table[x][y] = v

if __name__ == '__main__':
    table = SodukuTable()
    for x in range(0, 8):
        for y in range(0, 8):
            print table.get_v(x, y),
        print

