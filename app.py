#Author: H. M. Tarek Ullah


import pyrebase
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

config = {
  "apiKey": "##############",         #API key is hidden for security purpose 
  "authDomain": "your_project_name.firebaseapp.com",
  "databaseURL": "https://your_project_name.firebaseio.com",
  "storageBucket": "your_project_name.appspot.com",
  "serviceAccount": "/home/tarek/Music/firetest/serviceAccountCredentials.json"  ## serviceAccount is optional
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("users").child("Tarek")
data = {"name": "Mortimer 'Tarek' Ullah"}
db.child("users").push(data)
db.child("users").child("Hossain")
dat = {"name" : "shuvo" , "score" : 600}
db.push(dat)
