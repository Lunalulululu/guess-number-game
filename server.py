from flask import Flask
from random import randrange

answer = randrange(10)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Guess a number between 0 and 9 </h1>'\
        '<p> Guess number by adding "/number" to the existing path above. For instance, guessing number 6 means adding "/6" to the existing path</p>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route("/<int:number>")
def check(number):
    if number < answer:
        return '<h1 style = "color:red">Too low, try again!</h1>'\
            '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    elif number > answer:
        return '<h1 style = "color:purple">Too high, try again!</h1>'\
            '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return '<h1 style = "color:green">You found me!</h1>'\
            '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'


if __name__ == "__main__":
    app.run()
