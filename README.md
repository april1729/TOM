# TOM
# Tic tactics Optimizing Machine

Tic Tactics is a game played on a 3x3 grid of 3x3 grids.  Each 3x3 grid is a game of tic-tac-toe.  The first person is free to move anywhere on the board, after that the player must move on the tic tac to board that corresponds to the place her opponent chose on their last move move.  The following would be an example of normal game play:
<\p>
Move 1:

      |       |
_|_|_ | _|_|x | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
      |       |      
      
      
Move 2:
      |       |
_|_|_ | _|_|X | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  |O|
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
      |       |      
      
Move 3:
      |       |
_|_|_ | _|_|X | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  |O|
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|X|_ | _|_|_
 | |  |  | |  |  | |
      |       |      
      
Move 4:
      |       |
_|_|_ | _|_|X | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  |O|
______|_______|______
      |       |
_|_|_ | _|O|_ | _|_|_
_|_|_ | _|_|_ | _|_|_
 | |  |  | |  |  | |
______|_______|______
      |       |
_|_|_ | _|_|_ | _|_|_
_|_|_ | _|X|_ | _|_|_
 | |  |  | |  |  | |
      |       |      
      
<\p>
And so on.  Once someone wins a small board, they earn that spot on the big board.  The first to get three in a row on the big board wins.

Tic tactics Optimizing Machine, or TOM, is an AI that simulates and (tries to) play the game optimally.  He uses minimaxing to choose his moves (https://en.wikipedia.org/wiki/Minimax).  

# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Tictactics Optimizing Machine</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">A. Sagan</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

TOM is the intelectual property of University of California, Merced.

