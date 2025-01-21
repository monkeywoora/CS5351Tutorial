def is_win1(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X'):
        win = True
    return win
def is_win2(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'O'):
        win = True
    return win

def main():
    print("Welcome to the Tic-Tac-Toe!")
    print("You can enter -1 -1 to end the game before the end of the game.")
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if i==j and i==-2 and j==-2:
            print("The game is over before the end of the game.")
            break
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        if is_win1(game):
            print("Player 1 Win!")
            break  # Terminate the game
        elif is_win2(game):
            print("Player 2 Win!")
            break
        if n == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board
        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()
    exit(0)
