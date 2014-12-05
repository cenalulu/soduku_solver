__author__ = 'michellezhou'
import copy



def get_next_pos(x, y):
    if y < 8:
        return x, y+1
    else:
        if x < 8:
            return x+1, 0
        else:
            return x, y

class Soduku():
    def __init__(self, origin_table):
        self.origin_table = copy.deepcopy(origin_table)
        self.__tmp_solve_table = copy.deepcopy(origin_table)

    def __is_confilict(self, pos_x, pos_y, v, table):
        for row in range(0, 9):
            if table[row][pos_y] == v:
                return True

        for col in range(0, 9):
            if table[pos_x][col] == v:
                return True

        div_x = pos_x/3
        div_y = pos_y/3
        for offset_x in range(0, 3):
            for offset_y in range(0, 3):
                if table[div_x*3+offset_x][div_y*3+offset_y] == v:
                    return True

        return False

    def solve(self, x_to_solve, y_to_solve, table_to_solve):
        (next_x, next_y) = get_next_pos(x_to_solve,y_to_solve)

        if self.origin_table[x_to_solve][y_to_solve] != 0:
            return self.solve(next_x, next_y, table_to_solve)
        else:
            all_failed = True
            for v_try in range(1, 10):
                if not self.__is_confilict(x_to_solve, y_to_solve, v_try, table_to_solve):
                    if x_to_solve == 8 and y_to_solve == 8:
                        self.__tmp_solve_table[x_to_solve][y_to_solve] = v_try
                        return True
                    tmp_table = copy.deepcopy(table_to_solve)
                    tmp_table[x_to_solve][y_to_solve] = v_try
                    if self.solve(next_x, next_y, tmp_table):
                        #we are trying the correct value for this point
                        all_failed = False
                        self.__tmp_solve_table[x_to_solve][y_to_solve] = v_try
                        break
                    else:
                        #it we set v_try for this point, there will be no result in the future
                        continue
                else:
                    #this number cannot be fill for this point now
                    pass
            if all_failed:
                return False
            else:
                return True

    def print_table(self):
        for x in range(0, 9):
            for y in range(0, 9):
                v = self.__tmp_solve_table[x][y]
                if v == 0:
                    print '_',
                else:
                    print v,
            print
        return True

if __name__ == '__main__':
    table = list()
    table.append([0, 0, 7, 3, 0, 0, 5, 0, 0])
    table.append([6, 4, 0, 0, 2, 5, 0, 0, 0])
    table.append([8, 0, 0, 4, 0, 0, 0, 3, 0])
    table.append([4, 0, 0, 0, 5, 0, 0, 0, 3])
    table.append([0, 0, 8, 0, 0, 0, 6, 0, 0])
    table.append([9, 0, 0, 0, 8, 0, 0, 0, 2])
    table.append([0, 9, 0, 0, 0, 2, 0, 0, 4])
    table.append([0, 0, 0, 1, 4, 0, 0, 5, 7])
    table.append([0, 0, 4, 0, 0, 6, 1, 0, 0])
    quiz = Soduku(table)
    quiz.solve(0,0,quiz.origin_table)
    quiz.print_table()

