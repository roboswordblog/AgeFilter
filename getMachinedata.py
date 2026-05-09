import torch


def loadModel(age):
    model = torch.load(f'{age}.pth')
    model.eval()
    return model
