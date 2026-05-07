from flask import Flask, render_template, request
from dataManage import *
# import main
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
        username = request.form["username"]
        password = request.form["password"]
        age = request.form.get("age", "0")  # optional

        addUsers(username, password, age)
        return render_template("home.html", username=username)


@app.route("/signupData", methods=["GET"])
def signupData():
    return {"takenUsers": getAllUsers()}
    
@app.route("/sendMessage", methods=["POST"])
def sendMessage():
    data = request.get_json()
    addMessage(data["sentName"], data["post"])
    return {"status": "ok"}
@app.route("/getAllData")
def getMessages():
    return {"messages": getAllMessages()}

@app.route("/verifyMessages")
def verifyMessages():
    # verify whether the messages are appropriate or inappropriate
    pass


app.run(debug=True)
