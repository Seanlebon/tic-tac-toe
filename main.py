from board import Board
from player import Player

def main():
    print("***********************")
    print("Welcome to tic-tac-toe!")
    print("***********************")
    # player_one_name = input("Player One enter name: ")
    # player_two_name = input("Player Two enter name: ")
    ROWS = 3
    COLS = 3
    player_one = Player("Player 1", "X", ROWS, COLS)
    player_two = Player("Player 2", "O", ROWS, COLS)

    board = Board(ROWS,COLS, player_one, player_two)
    turns = 0
    print(board.getBoard())

    while not board.win:
        curr_player = player_one if turns % 2 == 0 else player_two
        move = input(curr_player.name + " please enter a move (row, col): ")
        if move == "exit":
            print("Thanks for playing!")
            return
        move = move.replace(" ","").split(",")
        print()
        row, col = int(move[0]), int(move[1])
        if board.updateBoard(row, col, curr_player):
            turns+=1
        print(board.getBoard())
        board.checkWin()

        
    print()
    reset = input("Play Again?(Y/N): ")
    print()
    if reset.lower() == "y":
        print()
        main()
    return

if __name__ == "__main__":
    main()