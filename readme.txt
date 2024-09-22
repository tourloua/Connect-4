Remake of the popular game "Connect-4" in Python. Meant to be played by two players. Use the left and right keys to move your piece around. Use the down key to place your piece. Space bar exits the program.

Very minimalist design. All gameplay occurs in the terminal. 

Libraries used: os and readchar

CHANGELOG 09-22-2024
game is no longer case sensitive
patched VERY elusive bug where the player's active character would not change after a piece was placed until an arrow key was pressed
got rid of redundant code that would check the diagonal win conditions before it is mathematically possible to "win" diagonally
