from model import NeuralNet
import random
import torch
from json import load
from Utils import bag_of_word, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



with open("./intents.json") as f:
    intents = load(f)['intents']


FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()