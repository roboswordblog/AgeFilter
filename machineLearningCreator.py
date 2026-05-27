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
elif 14 <= age <= 17:
    ageGroup = "1417.csv"
else:
    ageGroup = "MA.csv" 

df = pd.read_csv(f"data/{ageGroup}")


vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["message"].astype(str)).toarray()
y = df["appropriate"]
input_size = X.shape[1]
X = torch.FloatTensor(X)




class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 100)
        self.fc2 = nn.Linear(100, 32)
        self.fc3 = nn.Linear(32, 16)
        self.fc4 = nn.Linear(16, 8)
        self.out = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = self.out(x)
        return x

y = torch.LongTensor(df["appropriate"].values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
torch.manual_seed(41)
model = Model()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# train it
epochs = 1500

for i in range(epochs):
    # get result
    y_pred = model(X_train)
    # get loss
    loss = criterion(y_pred, y_train)
    # reset gradient
    optimizer.zero_grad()
    # go backwards and fix everything
    loss.backward()
    optimizer.step()
    # print it out every 10 epochs
    if i % 10 == 0:
        predictions = torch.argmax(y_pred, dim=1)
        accuracy = (predictions == y_train).float().mean()
        print(accuracy)
# get the test results
with torch.no_grad():
    model.eval()
    test_outputs = model(X_test)
    predictions = torch.argmax(test_outputs, dim=1)
    accuracy = (predictions == y_test).float().mean()
    print(f"Test Accuracy: {accuracy.item():.4f}")
with torch.no_grad():
    model.eval()
appropriateMap = {
    1:"Approprate",
    0:"NONAPPROPRiATE"
}
user_input = input("\nEnter a message (or type 'quit' to stop): ")
input_vector = vectorizer.transform([user_input]).toarray()
input_tensor = torch.FloatTensor(input_vector)

with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1).item()

    print(f"Predicted: {appropriateMap[prediction]}")
torch.save(model.state_dict(), f'models/{ageGroup}.pth')
import pickle

with open(f"models/{ageGroup}_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
import json

config = {
    "input_size": input_size,
    "hidden1": 100,
    "hidden2": 32,
    "hidden3": 16,
    "hidden4": 8,
    "output_size": 2,
    "vectorizer_max_features": 500
}

with open(f"models/{ageGroup}_config.json", "w") as f:
    json.dump(config, f)
print("DONE")
