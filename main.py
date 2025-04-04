from ayoayo import Ayoayo

# Starting the game
game = Ayoayo()
#first player created automatically becomes player 1
#second player created automatically becomes player 2
game.createPlayer()
player = 1

while True:
    # Display the board and current player's turn
    game.printBoard()
    current_name = game.player1_name if player == 1 else game.player2_name
    print(f"{current_name}'s turn")

    try:
        pit = int(input(f"{current_name}, choose a pit (1-6): "))
        if pit < 1 or pit > 6:
            print("Invalid input. Please choose a number from 1 to 6.")
            continue

        if game.board[pit - 1 if player == 1 else pit + 5] == 0:
            print("Invalid play! Selected pit is empty. Choose a different pit.")
            continue

        # Execute move and get next player
        new_player = game.playGame(player, pit)
        player = new_player

        # Check if game is over
        if game.game_over():
            print("Game over!")
            game.printBoard()
            print(game.returnWinner())
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
