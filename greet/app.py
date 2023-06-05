from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/<variable>')
def welcoming(variable):
    return f"welcome {variable}"
# @app.route('/welcome/home')
# def welcome_home():
#     return f"welcome home"

# @app.route('/welcome/back')
# def welcome_back():
#     return f"welcome back"