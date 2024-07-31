import itertools
from colorama import init, Fore, Style
init()

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Diagonally (descending)
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags):
        print("Winner is (/) diagonal")
        return True

    # Diagonally (ascending)
    diags = []
    for i in range(len(current_game)):
        diags.append(current_game[i][i])
    if all_same(diags):
        print("Winner is (\\) diagonal")
        return True

    # Vertically
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print("Winner is vertically (|)")
            return True

    # Horizontally
    for row in current_game:
        if all_same(row):
            print("Winner is horizontally (-)")
            return True

    return False

def game_board(gamesize, game_map, player=0, row=0, column=0, just_display=False):
    try:
        if not just_display:
            if game_map[row][column] != 0:
                print("This place is already occupied!")
                return game_map, False
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)
        return game_map, True

    except Exception as e:
        print(f"An error occurred: {e}")
        return game_map, False

play = True
players = [1, 2]

while play:
    gamesize = int(input("Enter size of game Tic-Tac-Toe: "))
    s = "   "
    for i in range(gamesize):
        s += "  " + str(i) + " "
    print(s)
    game = [[0 for i in range(gamesize)] for i in range(gamesize)]

    game_won = False
    game, _ = game_board(gamesize, game, just_display=True)
    player_choice = itertools.cycle(players)

    while not game_won:
        current_player = next(player_choice)
        print(f"\nPlayer {current_player}'s turn")

        played = False
        while not played:
            column_choice = int(input("Enter column: "))
            row_choice = int(input("Enter row: "))
            if 0 <= column_choice < gamesize and 0 <= row_choice < gamesize:
                game, played = game_board(gamesize, game, current_player, row_choice, column_choice)
                if not played:
                    print("Invalid move! Try again.")
            else:
                print("Invalid input! Enter values within the range.")

        if win(game):
            game_won = True
            again = input("Do you want to play again (y/n)? ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                play = False
                print("See you later!")
            else:
                print("Invalid input! Exiting the game.")
                play = False
