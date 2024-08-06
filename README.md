## Draughts
This is a simple launcher for python draughts bots.
## Installation
```
git clone https://github.com/DeltaElim/draughtsjudge
cd draughtsjudge
```
The program requires pygame in order to run.
```
pip install pygame
```
## Bot requirements
Your script must contain a ```main``` function, which receives an 8x8 array with the current board position. The numbers in the array have the following meaning:
```
0 - empty
1 - white
2 - white crowned
3 - black
4 - black crowned
```
This is what the starting position looks like:
```
[
[0, 3, 0, 3, 0, 3, 0, 3],
[3, 0, 3, 0, 3, 0, 3, 0],
[0, 3, 0, 3, 0, 3, 0, 3],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0]]
```
Your pieces will always appear white in the position the script receives, regardless of its assigned color on the board.  
Your script must return a four-digit integer (or a three-digit one if the first digit is 0), where:  
The first digit corresponds to the y coordinate of the position the move was made **from**, from top to bottom, starting at zero  
The second digit corresponds to the x coordinate of the position the move was made **from**, from left to right, starting at zero  
The third digit corresponds to the y coordinate of the position the move was made **to**, from top to bottom, starting at zero  
The fourth digit corresponds to the x coordinate of the position the move was made **to**, from left to right, starting at zero  
An example of a valid first move by white pieces would be ```5041```, which would look like ```2736``` to the black pieces.
## Launching
Although there is a 'Browse' option in the applicaton, it requires restarting the program before launching the bots for the first time. The alternative is to copy your scripts in the same folder as the application and naming the files 'bot_A.py' and 'bot_B.py'
The 'Play' button autoplays the game with an interval of 0.2 seconds between moves. Pressing 'Stop' will stop the autoplay, and pressing 'Reset' will reset the board to the starting position. Clicking on the board advances the game move by move. Journal on the side displays past moves in the notation described above.  
Press 'Exit' or close the window to exit the application.
