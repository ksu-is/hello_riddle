from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def greet():

    user_input = request.form['guess']
    user_input = user_input.capitalize()

    return render_template ("home.html", guess=user_input)

@app.route('/')
def home():
    
    return render_template("home.html")


if __name__ == '__main__':
        app.run(debug=True)
        