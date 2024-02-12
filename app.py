from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
        {
          'author': 'David Sexton',
           'title': 'Blog Post 1',
            'content': 'First post' ,
            'date': '10/01/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 2',
            'content': 'Second post' ,
            'date': '12/01/24',
        },
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__mainn__':
        app.run(debug=True)