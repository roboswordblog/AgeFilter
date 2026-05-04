import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

age = int(input("What is your age? "))
ageGroup = ""
if 5 <= age <= 8:
    ageGroup = "58.csv"
elif 9 <= age <= 13:
    ageGroup = "913.csv"
elif 14 <= x <= 17:
    ageGroup = "1417.csv"
else:
    ageGroup = "MA.csv" 

df = pd.read_csv(f"/data/{ageGroup}")


vectorizer = TfidfVectorizer(max_features=500)




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


