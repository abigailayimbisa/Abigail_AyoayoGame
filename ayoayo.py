class Ayoayo:
    # Ayoayo game class
    # This class represents the Ayoayo game, including the board, players.
    def __init__(self):
        self.board = [4] * 12  # 12 pits, 4 seeds each
        self.score1 = 0
        self.score2 = 0
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"


    # Initialize players with default names
    def createPlayer(self):
        self.player1_name = input("Enter Player 1's name: ")
        self.player2_name = input("Enter Player 2's name: ")

    # Initialize the board with 4 seeds in each pit and print the states at any given step
    def printBoard(self):
        top_row = '  '.join(str(self.board[i]) for i in range(11, 5, -1))
        bottom_row = '  '.join(str(self.board[i]) for i in range(0, 6))
        print("\n" + self.player2_name + " side")
        print("  " + top_row)
        print("  " + bottom_row)
        print(self.player1_name + " side\n")
        print(f"Score -> {self.player1_name}: {self.score1} | {self.player2_name}: {self.score2}\n")


    #this method allows players to choose pits which are not empty and sow 
    def playGame(self, player, pit_index):
        pit_index -= 1  # Convert 1-6 input to 0-5 index
        if player == 2:
            pit_index += 6

        if self.board[pit_index] == 0:
            print("Invalid play! Selected pit is empty. Choose a different pit.")
            return player  # Same player tries again

        seeds = self.board[pit_index]
        self.board[pit_index] = 0
        current_index = pit_index


        # this loop allows the player to sow seeds in the selected pit and capture seeds from the opposite pit
        # until the last seed lands on a pit with seeds or an empty pit
        # and captures seeds from the opposite pit if available
        while True:
            # Sow seeds
            while seeds > 0:
                current_index = (current_index + 1) % 12
                self.board[current_index] += 1
                seeds -= 1

            # If last seed lands on a non-zero pit, continue from that pit
            if self.board[current_index] > 1:
                seeds = self.board[current_index]
                self.board[current_index] = 0
                continue

            # Landed on zero pit, capture from opposite
            opposite_index = 11 - current_index
            captured = self.board[opposite_index]
            if captured > 0:
                print(f"{self.player1_name if player == 1 else self.player2_name} captures {captured} from opposite pit.")
                self.board[opposite_index] = 0  # Remove captured seeds
                if player == 1:
                    self.score1 += captured
                else:
                    self.score2 += captured
            break  # End turn when you land on zero

        return 2 if player == 1 else 1
    
    #this method checks if the game is over and distributes remaining seeds to the respective players
    def game_over(self):
        """Check if the game should end (i.e., all pits on one side are empty)."""
        side1_empty = all(seeds == 0 for seeds in self.board[:6])
        side2_empty = all(seeds == 0 for seeds in self.board[6:])

        if side1_empty or side2_empty:
            # Distribute remaining seeds to the respective players
            self.score1 += sum(self.board[:6])
            self.score2 += sum(self.board[6:])
            self.board = [0] * 12  # Clear board
            return True
        return False
    
    #this method returns the winner based on the highest score and a tie if scores are equal
    def returnWinner(self):
        """Determine the winner based on the highest score."""
        if self.score1 > self.score2:
            return f"{self.player1_name} wins!"
        elif self.score2 > self.score1:
            return f"{self.player2_name} wins!"
        else:
            return "It's a tie!"
