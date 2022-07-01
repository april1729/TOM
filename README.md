# TOM
# Tictactics Optimizing Machine

Tictactics is a game played on a 3x3 grid of 3x3 grids.  Each 3x3 grid is a game of tic-tac-toe.  The first person is free to move anywhere on the board, after that the player must move on the tic-tac-toe board that corresponds to the place her opponent chose on their last move move.  <a rel="Here" href="http://mathwithbaddrawings.com/ultimate-tic-tac-toe-original-post/"> Here <a> is a better explination.

Tictactics Optimizing Machine, or TOM, is an AI that simulates and (tries to) play the game optimally.  It uses the [minimax](https://en.wikipedia.org/wiki/Minimax) to choose its moves .  The game is played in a web browser using Flask, and you can play it at (https://tom.aprilsagan.net).

# Running the server locally 

To run locally on a linux machine,

```
git clone https://github.com/april1729/TOM.git
cd TOM
export FLASK_APP application.py
flask run
```


# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Tictactics Optimizing Machine</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">A. Sagan</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

