from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/home', methods=['POST'])
def index():
    answer = request.form['guess']

    
    if "Hello World!" in answer or "Hello World"  in answer:
        return render_template("index.html", guess = "correct")

    else:
        return render_template("index.html",guess="incorrect")
    
    

@app.route('/')
def home():
        return render_template('index.html')


if __name__ == "__main__":
    app.run( debug = True)