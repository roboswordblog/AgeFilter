def getAllUsers():
    files = open("webData/users.csv", "r")
    users = []
    for line in files.read().split("\n"):
        users.append(line.split(",")[0])
    return users

def addUsers(username,password,age):
    files = open("webData/users.csv", "a")
    files.write(f"{username},{password},{age}")

def checkUsers():
    pass