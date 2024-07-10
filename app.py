from flask import Flask, render_template, request, redirect, url_for, flash, session
from handle_sql import *

from flask_session import Session

app = Flask(__name__)
# setting session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# home + function
@app.route('/',  methods=['GET'])
def home():
    session["username"] = None
    return render_template("home.html")
      
# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': 
        session["username"] = None
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        # check admin - user - wrong pass
        key = check_password(username, password)
        if key == 0: # admin id
            # return redirect(url_for('user', name = username, key = key))
            session["username"] = username
            return redirect(url_for('admin'))
        elif key > 0: # user id
            session["username"] = username
            return redirect(url_for('user', username = username))
        else:
            return render_template("login.html", Notice = "Wrong username or password")

# Register
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # check user exited
        username = request.form['username']
        mail = request.form['mail']
        password = request.form['password']
        if check_username_not_exited(username):
            add_user(username, mail, password)
            return render_template("register.html", Notice = "Register successful")
        else:
            return render_template("register.html", Notice = "Username exited")

# take password
@app.route('/forgot', methods = ['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template("forgot.html", notice = "")
    else:
        username = request.form['username']
        email = request.form['mail']
        if take_password(username, email) == 0:
            return render_template("forgot.html", notice = "Wrong username or email")
        elif take_password(username, email) == -1:
            return render_template("forgot.html", notice = "Your account isn't exit")
        else:
            return render_template("forgot.html", notice = f"Your password is: {take_password(username, email)}")

# admin
@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if session["username"] != "admin":
        return "Not permision"
    else:
        if request.method == "GET":
            data = get_data()
            return render_template('admin.html', data=data)
        else:
            session['username'] = None
            return redirect(url_for('home'))
        
# user
@app.route('/user/<username>', methods = ['GET', 'POST'])
def user(username):
    if session["username"] == username and username != "admin":
        if request.method == "POST":
            session['username'] = None
            return redirect(url_for('home'))
        else:
            return render_template("user.html", name = username)
    else:
        return "Not permision"
    

if __name__ == '__main__':
    app.run(debug=True)
