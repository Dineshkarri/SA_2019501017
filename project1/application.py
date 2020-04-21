import os
import datetime
from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

# Tell Flask what SQLAlchemy database to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database
db.init_app(app)


@app.route("/")
def index():
    return render_template("register.html", flag=True)

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method == "POST"):
        username = request.form.get("uname")
        password = request.form.get("pswd")
        dt = datetime.datetime.now()
        
        if not username:
            text = "Please enter username to register"
            return render_template("usernames.html", name=text, msg="ERROR")
        elif not password:
            text="Please provide password"
            return render_template("usernames.html", name=text ,msg="ERROR")
        else:
            data2 = Data.query.all()
            for user in data2:
                if username == user.Username:
                    return "<h2 Style='color: red;text-align:center'>You already have registered !Please Login </h2>"
            data = Data(Username=username,Password=password,Timestamp=dt)
            db.session.add(data)
            db.session.commit()
            return render_template("usernames.html",msg="SUCCESS")
    return render_template("register.html", flag=True)

@app.route("/admin")
def admin():
    data1 = Data.query.all()
    return render_template("userlist.html", name=data1)

@app.route("/auth",methods=["GET","POST"])
def userhome():
    if (request.method == "POST"):
        username = request.form.get("uname")
        password = request.form.get("pswd")
        if not username:
            text = "Please enter username to register"
            return render_template("usernames.html", name=text, msg="ERROR")
        elif not password:
            text="Please provide password"
            return render_template("usernames.html", name=text ,msg="ERROR")
        data3 = Data.query.all()
        for user in data3:
            if user.Username == username:
                if user.Password == password:
                    session["username"]= user.Username
                    return redirect("/user")
        return render_template("register.html",flag=False)
    if (request.method == "GET"):
        return redirect(url_for('register'))

@app.route("/logout")
def sessiontimeout():
    session.pop("username",None)
    return redirect(url_for('register'))

@app.route("/user")
def user():
    if session.get("username") is not None:
        return render_template("user.html")
    return redirect(url_for('register'))



def main():
    app.app_context().push()
    db.create_all()



if __name__ == "__main__":
    # with app.app_context():
    main()