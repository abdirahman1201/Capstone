from capstone import app
from flask import render_template


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/account')
def account():
    return render_template('account.html', title='Account')

@app.route('/register', methods=['POST','GET'])
def register():
    form=RegistrationForm()
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    return render_template('login.html', title='login')

