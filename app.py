from flask import Flask, render_template, request

app  = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["Get", "Post"])
def login():
    if request.methods == "GET":
        return render_template("login.html")
    elif request.methods == "POST":
        # add the datamanage later
        return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    pass

@app.route("/signupData", methods=["GET"])
def signupData():
    return {"takenUsers": ["BOBBY", "CHACHA", "Robosword"]}
