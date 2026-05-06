from flask import Flask, render_template, request
from dataManage import *
app  = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["Get", "Post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        return render_template("home.html")
    return None


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    elif request.method == "POST":
        return render_template("home.html")


@app.route("/signupData", methods=["GET"])
def signupData():
    return {"takenUsers": getAllUsers()}

@app.route("/sendMessage")
def sendMessage():
    # add the message to the rest of the messages in the file along with the username
    pass

@app.route("/getAllMessages")
def getMessages():
    # get all the messages from the file and see which ones the frontend doesn't have
    pass


app.run(debug=True)
