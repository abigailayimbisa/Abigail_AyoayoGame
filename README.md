# Abigail_AyoayoGame
Ayoayo Game Implementation using Python
1.	Approach  
I implemented the Ayoayo game using Python. The game logic is designed to follow the traditional rules provided for the game which ensures that players take turns, distribute seeds correctly, and capture seeds when the conditions are met.  
•	The `Ayoayo` class manages the game board, rules, player turns, and capturing mechanics.  
•	The `main.py` script is responsible for getting player input, running the game loop, and displaying the board.  
•	The reflection.txt file captures my thought process and understanding of the game

2.	Assumptions

•	The game follows a counter-clockwise distribution of seeds.  
•	Each player has 6 pits and 1 store, making 12 pits and 2 stores in total.  
•	Each pit starts with 4 seeds, giving a total of 48 seeds in the game.  
•	Players must select a non-empty pit on their turn.  
•	If a player's last seed lands in an empty pit on their side, they capture the single seed in their own pit and all the seeds in the opponent’s opposite pit. 
•	The game ends when a player has no seeds left in all 6 pits.  
•	The winner is the player with the most seeds in their store.  
•	A draw occurs if both players collect 24 seeds each.  
•	A player continues to play if the last seed drops in a non-empty pit, he/she picks all the seeds and continues distributing.

3.	How to Run the Game

download the code as a zip file from this repository 
Install VSCode  if not already installed
install the necessary extensions in VSCode
Then upload the extracted folder from the inital zip file
run main.py in the terminal

