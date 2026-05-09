from flask import Flask, render_template, request
from dataManage import *
import getMachinedata

app = Flask(__name__)
age = 0

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    global age
    if request.method == "GET":
        return render_template("signup.html")

    elif request.method == "POST":
        username = request.form["username"]
        age = request.form.get("age", "0")
        addUsers(username, age)
        return render_template("home.html", username=username)
    return None


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


if __name__ == "__main__":
    app.run(debug=True)
