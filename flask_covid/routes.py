from flask import render_template,url_for,flash,redirect
from flask_covid import app,db,bcrypt
from flask_covid.forms import RegistrationForm, LoginForm
from flask_covid.models import User,Post


posts=[
    {
        'author':'Siddharth Sharma',
        'title':'Post-Graph1',
        'content':'Number of cases',
        'date':'September 2021',

    },
     {
        'author':'John Doe',
        'title':'Post-Graph2',
        'content':'Number of cases in 2nd wave',
        'date_posted':'October 2021',

    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash('form.passeord.data').decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Username and Password','danger')
    return render_template('login.html',title='Login',form=form)