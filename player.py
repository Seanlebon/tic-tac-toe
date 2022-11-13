class Player:
    def __init__(self, player_name, player_sym, rows, cols):
        self.name = player_name
        self.sym = player_sym
        self.ROWS = rows
        self.COLS = cols
        self.diag1_count = 0
        self.diag2_count = 0
        self.rows_count = [0] * rows
        self.cols_count = [0] * cols
    def makeMove(self, row, col):
        if row == col:
            self.diag1_count+=1
        if row + self.COLS-1 == col:
            self.diag2_count+=1

        self.rows_count[row] += 1
        self.cols_count[col] += 1
    def isWin(self):
        if self.diag1_count == 3:
            return True
        if self.diag2_count == 3:
            return True
        for row_count in self.rows_count:
            if row_count == 3:
                return True
        for col_count in self.cols_count:
            if col_count == 3:
                return True
        return False
