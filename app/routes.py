from app.forms import RegisterForm
from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Corron'
    title = " Coding temple"
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
    return render_template('register.html', title="Register for CT Blog", form=form)
    