from flask import Flask
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def index():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

if __name__ == '__mainn__':
        app.run(debug=True)