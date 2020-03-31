from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/myFirstPage')
def new_function():
    return "hello hello"

@app.route('/pickRock')
def buildMyPage():
    output = 0
    number_list = [1,2,3,4,5]
    for i in number_list:
        output += i
    return render_template("rock.html", numberSum=output)

@app.route('/pickPaper')
def buildMyPaperPage():
    return render_template("paper.html")

@app.route('/pickScissors')
def buildMyScissorPage():
    return render_template("scissors.html")