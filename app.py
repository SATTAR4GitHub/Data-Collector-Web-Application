"""
This is a maun python script for collecting data from the user. This progam renders
index.html and success.html files.
Author: Abdus Sattar Mia
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from return_email import sendEmail


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres100@localhost/data_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="client_data"
    id=db.Column(db.Integer, primary_key=True)
    name_=db.Column(db.String(50))
    email_=db.Column(db.String(120),unique=True)

    def __init__(self, name_, email_):
        self.name_=name_
        self.email_=email_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method =='POST':
        name = request.form["name"]
        email = request.form["email_name"]
        sendEmail(name, email)
        if db.session.query(Data).filter(Data.email_==email).count()==0:
            data=Data(name, email)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template('index.html',
    comment="Sorry, this email already exists!")

if __name__=='__main__':
    app.debug=True
    app.run()
