from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page route"

@app.route("/about")
def about():
    return "about page route"

@app.route("/contact")
def contact():
    return "contatos route"

@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text

