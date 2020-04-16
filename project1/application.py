import os

from flask import Flask, session, render_template, request
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
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Tell Flask what SQLAlchemy database to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database
# db.init_app(app)

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method == "POST"):
        username = request.form.get("uname")
        print(username)
        password = request.form.get("pswd")
        print(password)
        return render_template("usernames.html", name=username)
    return render_template("register.html")

def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()