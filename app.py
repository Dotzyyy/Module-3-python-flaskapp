from flask import Flask, render_template, url_for, flash, redirect
from forms import NewUserForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3b6a520a6f67388f4e02bdc1fa18c4c3'

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

@app.route("/registration", ['GET', 'POST'])
def registration():
    form = NewUserForm()
    if form.validate_on_submit():
         flash(f'Account created for {form.username.data}!', 'success')
         return redirect(url_for('index'))
    return render_template('registration.html', title='Registration', form='form')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form='form')

if __name__ == '__mainn__':
        app.run(debug=True)