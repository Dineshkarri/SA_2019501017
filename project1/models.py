from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    __tablename__ = "USERS database table"
    Username = db.Column(db.String, primary_key=True, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Timestamp = db.Column(db.String, nullable=False)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    pub_year = db.Column(db.Integer, nullable=False)


class Review(db.Model):
    __tablename__ = "reviews"
    isbn = db.Column(db.Integer, nullable = False)
    username = db.Column(db.String, nullable = False)
    rating = db.Column(db.Integer, nullable = True)
    review = db.Column(db.String, nullable =True)
    isbnusername = db.Column(db.String, primary_key =True, nullable =False)

