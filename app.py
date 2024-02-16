from flask import Flask, render_template, url_for, flash, redirect
from forms import NewUserForm, LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



posts = [
        {
          'author': 'David Sexton',
           'title': 'Blog Post 1',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ornare nibh finibus sapien vehicula, eget pulvinar turpis porttitor.',
            'date': '10/01/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 2',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '12/01/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 3',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '19/01/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 4',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '22/01/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 5',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ornare nibh finibus sapien vehicula, eget pulvinar turpis porttitor.',
            'date': '01/02/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 6',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '04/02/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 7',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '15/02/24',
        },
        {
          'author': 'David Sexton',
           'title': 'Blog Post 8',
            'content': 'Morbi nisi lectus, tempor eu ornare a, dapibus vel risus. Ut vitae diam eget massa dictum vestibulum vitae a metus. Sed volutpat mi lectus, sit amet posuere justo commodo non. Vivamus sed erat volutpat, vehicula mi et, iaculis augue. Cras porta lacus ac scelerisque vulputate. Nunc fermentum, velit et suscipit commodo, justo ligula dapibus ante, in ullamcorper dolor sapien sit amet lectus. Etiam scelerisque tortor in mollis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' ,
            'date': '20/02/24',
        },
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    form = NewUserForm()
    if form.validate_on_submit():
         flash(f'Welcome, {form.username.data}!', 'success')
         return redirect(url_for('index'))
    return render_template('registration.html', title='Registration', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
         else:
              flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__mainn__':
        app.run(debug=True)