from player import Player
class Board:
    def __init__(self, rows, cols, player_one, player_two):
        self.ROWS = rows
        self.COLS = cols
        self.board = [["_"]*cols for _ in range(rows)]
        self.moves = set()
        self.player_one = player_one
        self.player_two = player_two
        self.win = False
    
    def updateBoard(self, row, col, player):
        if (row,col) in self.moves:
            print()
            print("This move has already been made on the board!")
            return False
        player.makeMove(row,col)
        self.board[row][col] = player.sym
        self.moves.add((row,col))
        return True

    def checkWin(self):
        if self.player_one.isWin():
            print(self.player_one.name, "WINS!!!")
            self.win = True
        if self.player_two.isWin():
            print(self.player_two.name, "WINS!!!")
            self.win = True

    def getBoard(self):
        return_string = ""
        for i in range(self.ROWS):
            for j in range(self.COLS):
                return_string += self.board[i][j] + " "
            return_string +="\n"
        return return_string
    
    

