def getAllUsers():
    files = open("webData/users.csv")
    users = []
    for line in files.read().split("\n"):
        users.append(line.split(",")[0])
    return users

def addUsers():
    pass

def checkUsers():
    pass