import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split

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

class Model(nn.Model):
    pass
