from flask import Flask, render_template

import random
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/myFirstPage')
def new_function():
    return "hello hello"

SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']
selections_list = SELECTIONS_LIST_RPS
WIN_LIST_RPS = [('ROCK', 'SCISSORS'),
                ('SCISSORS', 'PAPER'),
                ('PAPER', 'ROCK')]


def computer_selection():
    computer_selection = random.choice(selections_list)
    return computer_selection

@app.route('/playGame/<user_input>')
def buildMyPage(user_input):
    computer = computer_selection()
    picked=user_input.upper()
    result = results(picked, computer)
    
    return render_template("playGame.html", pick=picked, comp=computer, result=result)

def results(user, computer):
    if user==computer:
        return "TIE!! Play again!"
    if user== "ROCK": 
        if computer == "PAPER":
            return "Computer Won"
        else: 
            return "You Won! Congrats!"
    if user == "PAPER":
        if computer == "SCISSORS":
            return "Computer Won"
        else: 
            return "You Won! Congrats!"
    if user == "SCISSORS":
        if computer == "ROCK":
            return "Computer Won"
        else: 
            return "You Won! Congrats!"
        return "Testing"

