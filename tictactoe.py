import random

def ConstBoard(board):
    print("Current state of the Board:\n\n")
    for i in range(0, 9):
        if ((i > 0) and (i % 3 == 0)):
            print("\n")
        if board[i] == 0:
            print("_", end=" ")
        elif board[i] == -1:
            print("X", end=" ")
        elif board[i] == 1:
            print("O", end=" ")
    print("\n\n")

def User1Turn(board):
    pos = input("Enter X's position from 1 to 9: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Wrong move")
        exit(0)
    board[pos - 1] = -1

def User2Turn(board):
    pos = input("Enter O's position from 1 to 9: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Wrong move")
        exit(0)
    board[pos - 1] = 1

def analyzeboard(board):
    # Add your logic to check the game state (win, lose, draw)
    # Return 0 for no result, -1 for X wins, 1 for O wins, 2 for draw
    return 0

def CompTurn(board):
    # Add your logic for computer's move
    # For example, you can randomly choose an empty position
    empty_positions = [i for i in range(9) if board[i] == 0]
    if empty_positions:
        comp_pos = random.choice(empty_positions)
        board[comp_pos] = 1

def main():
    choice = input("Enter 1 for single player and 2 for multiplayer: ")
    choice = int(choice)
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == 1:
        print("Computer: O vs You: X")
        player = input("Enter to play 1(st) or 2(nd): ")
        player = int(player)

        for i in range(0, 9):
            if analyzeboard(board) != 0:
                break
            if (i + player) % 2 == 0:
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)

    else:
        for i in range(0, 9):
            if analyzeboard(board) != 0:
                break
            if i % 2 == 0:
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    result = analyzeboard(board)
    ConstBoard(board)

    if result == 0:
        print("oh gawdd! It's a draw")
    elif result == -1:
        print("Hurrah!!!!!!Player X wins")
    elif result == 1:
        print("Hurrah!!!!!Player O wins")

if __name__ == "__main__":
    main()
