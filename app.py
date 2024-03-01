from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

# db=SQLAlchemy(app)

# class User(db.Model):
    # id=db.Column(db.Integer, primary_key=True)
    # name=db.Column(db.String(20))
    # email=db.Column(db.String(30), unique=True, index=True)
    

if __name__== "__main__":
    app.run(debug=True)    