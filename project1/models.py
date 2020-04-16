from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    __tablename__ = "USERS database table"
    Username = db.Column(db.String, primary_key=True, nullable=False)
    Password = db.Column(db.String, nullable=False)