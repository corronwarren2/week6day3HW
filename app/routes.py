from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterForm
from app.models import User


@app.route('/')
def index():
    name = 'Corron'
    title = " Coding temple"
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    print(form.username)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        #create new instance of User
        new_user = User(username, email, password)

        #add new user to
        db.session.add(new_user)
        db.session.commit()

        # once mew_user os added to db, flash success message
        flash(f'Thank you for signing up {new_user.username}!', 'primary')

        #redirect user back to home page
        return redirect(url_for('index'))
        
    return render_template('register.html', title="Register for CT Blog", form=form)
    