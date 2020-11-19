from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/home', methods=['POST'])
def index():
    inputName = request.form['myName']

    guess = input("Enter You Best Guess: ")

    if "Hello World!" or "Hello World"  in guess:
       print ("Hello World! How Are You Today?")
       print ("Click Here To Find Out :add link")

    inputName = inputName.upper()+" hi!  Visiting from "
    return render_template("index.html",myName=inputName)

@app.route('/')
def home():
        return render_template('index.html')


if __name__ == "__main__":
    app.run( debug = True)