import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def encodeAppropriate(x):
    if x == "Yes":
        return 1.0
    else:
        return 0.0

age = int(input("What is your age? "))
ageGroup = ""
if 5 <= age <= 8:
    ageGroup = "58.csv"
elif 9 <= age <= 13:
    ageGroup = "913.csv"
elif 14 <= age <= 17:
    ageGroup = "1417.csv"
else:
    ageGroup = "MA.csv" 

df = pd.read_csv(f"/data/{ageGroup}")


vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["message"].astype(str)).toarray()
y = df["appropriate"].apply(encodeAppropriate)




class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(300, 32)
        self.fc2 = nn.Linear(32, 32)
        self.fc3 = nn.Linear(32, 16)
        self.out = nn.Linear(16, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.out(x)
        return x

X = torch.FloatTensor(X)
y = torch.LongTensor(df["sentiment"].apply(encodeAppropriate).values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
