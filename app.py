from flask import Flask, render_template, request

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
    return {"takenUsers": ["BOBBY", "CHACHA", "Robosword"]}

app.run(debug=True)
