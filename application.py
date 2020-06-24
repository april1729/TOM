from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
from Board import Board
from Move import Move
import numpy
import math
from TOM import *

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = Board(1)
        session["mainGame"]= session["board"].mainBoardMatrix
        session["game"]=session["board"].getBoardTensor()
        session["validMove"]=session["board"].getValidMoves()
        session["turn"] = "X"
        session["winner"] = session["board"].isGameOver
        session["draw"] = False
        session["turnNum"] = 0


    if session["turnNum"]>0:
        session["board"].makeMove(getMinimaxMove(session["board"], 4))

    session["mainGame"]= session["board"].mainBoardMatrix
    session["game"]=session["board"].getBoardTensor()
    session["validMove"]=session["board"].getValidMoves()

    if session["board"].whoseTurn==1:
        session["turn"] = "X"
    else:
        session["turn"] = "O"

    winner = winnerFound(session["board"])
    if(winner[0] == True):
        session["winner"] = True
        session["turn"] = winner[1]
        print("winner found",session["winner"], session["turn"])

    if(winner[0] == False and winner[1] == "draw"):
        session["draw"] = True

    session["turnNum"]+=1
    return render_template("index.html", game=session["game"],validMove=session["validMove"],mainGame=session["mainGame"], turn=session["turn"],winnerFound=session["winner"],winner=session["turn"],draw=session["draw"])






@app.route("/play/<int:ro>/<int:co>/<int:ri>/<int:ci>")
def play(ro, co, ri, ci):
	session["board"].makeMove(Move(session["board"].whoseTurn, 3 * co + ro, 3 * ci + ri))

	return redirect(url_for("index"))

@app.route("/reset")
def reset():
    session["board"] = Board(1)
    session["mainGame"]= session["board"].mainBoardMatrix
    session["game"]=session["board"].getBoardTensor()
    session["validMove"]=session["board"].getValidMoves()
    session["turn"] = "X"
    session["winner"] = session["board"].isGameOver
    session["draw"] = False
    return redirect(url_for("index"))

def winnerFound(board):
	return [board.isWon(board.mainBoardMatrix), board.whoIsWinner()]





