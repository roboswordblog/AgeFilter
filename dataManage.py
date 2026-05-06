def getAllUsers():
    files = open("webData/users.csv", "r")
    users = []
    for line in files.read().split("\n"):
        users.append(line.split(",")[0])
    files.close()
    return users

def addUsers(username,password,age):
    files = open("webData/users.csv", "a")
    files.write(f"{username},{password},{age}\n")
    files.close()

def addMessage(user, message):
    files = open("webdata/chatLogs.csv", "a")
    files.write(f"{user},{message}\n")
    files.close()


def checkUsers():
    pass