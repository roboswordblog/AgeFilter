import torch
import torch.nn as nn
import torch.nn.functional as F
import pickle
import json


class Model(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 100)
        self.fc2 = nn.Linear(100, 32)
        self.fc3 = nn.Linear(32, 16)
        self.fc4 = nn.Linear(16, 8)
        self.out = nn.Linear(8, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        return self.out(x)


def loadModel(ageGroup):
    with open(f"models/{ageGroup}_config.json", "r") as f:
        config = json.load(f)

    input_size = config["input_size"]

    model = Model(input_size)
    model.load_state_dict(torch.load(f"models/{ageGroup}.pth"))
    model.eval()
    return model, input_size


def loadVectorizer(ageGroup):
    with open(f"models/{ageGroup}.pth", "rb") as f:
        return pickle.load(f)

def runModel(ageGroup, message):
    vectorizer = loadVectorizer(ageGroup)
    model, input_size = loadModel(ageGroup)

    label_map = {
        0: "NONAPPROPRIATE",
        1: "APPROPRIATE"
    }

    x = vectorizer.transform([message]).toarray()
    x = torch.FloatTensor(x)

    with torch.no_grad():
        out = model(x)
        pred = torch.argmax(out, dim=1).item()

    return label_map[pred]