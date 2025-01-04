import random


class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        print(self.matrix)
        self.add_new()

    def check_game_state(self):
        """zwraca stan gry"""
        for row in self.matrix:
            if 2048 in row:
                return "win"

        # czy sa puste miesjca
        for row in self.matrix:
            if 0 in row:
                return "continue"

        # czy sasiednie komorki maja takie same wartosci
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return "continue"
            for j in range(self.size - 1):
                if self.matrix[j][i] == self.matrix[j + 1][i]:
                    return "continue"

        # jesli zadne nie spelnione to przegrana
        return "lose"

    def get_max_value(self):
        """zwraca najwieksza wartosc w macierzy"""
        max_value = 0
        for row in self.matrix:
            max_value = max(max(row) for row in self.matrix)
        return max_value

    def add_new(self):
        """dodanie nowe komorki o wartosci 2"""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.matrix[i][j] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.matrix[x][y] = 2

    def reverse(self):
        """odwraca wiersze"""
        self.matrix = [row[::-1] for row in self.matrix]

    def transpose(self):
        """transopozycja"""
        self.matrix = [[self.matrix[j][i] for j in range(self.size)] for i in range(self.size)]

    def merge(self):
        """laczy komorki o tej samej wartosci w lewo"""
        changed = False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1] and self.matrix[i][j] != 0:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    changed = True
        return changed

    def cover_up(self):
        """przesuwa wszystko w lewo usuwajac zera zera."""
        new_matrix = [[0] * self.size for _ in range(self.size)]
        changed = False

        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.matrix[i][j] != 0:
                    new_matrix[i][count] = self.matrix[i][j]
                    if j != count:
                        changed = True
                    count += 1
        self.matrix = new_matrix
        return changed

    def move_left(self):
        """lewo cover_up merge cover_up"""
        cover_changed = self.cover_up()
        merge_changed = self.merge()
        if merge_changed:
            self.cover_up()
        if cover_changed or merge_changed:
            self.add_new()

    def move_right(self):
        """prawo reverse left reverse"""
        self.reverse()
        self.move_left()
        self.reverse()

    def move_up(self):
        """gora transpose left transpose."""
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        """dol transpose right transpose."""
        self.transpose()
        self.move_right()
        self.transpose()
