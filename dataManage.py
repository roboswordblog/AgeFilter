def getAllUsers():
    files = open("webData/users.csv", "r")
    users = []
    for line in files.read().split("\n"):
        users.append(line.split(",")[0])
    files.close()
    return users

def addUsers(username,password,age):
    files = open("webData/users.csv", "a")
    files.write(f"\n{username},{password},{age}")
    files.close()

def addMessage(user, message):
    files = open("webData/chatLogs.csv", "a")
    files.write(f"\n{user},{message}")
    files.close()


def checkUsers():
    pass