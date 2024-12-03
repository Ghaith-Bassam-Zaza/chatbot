from model import NeuralNet
import random
import torch
from json import load
from Utils import bag_of_word, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



with open("./intents.json") as f:
    intents = load(f)


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

bot_name = "Foulan"
print("Let's chat! type 'quit' to exit.")
while True:
    sentence = input("You: ")
    if sentence =="quit":
        break
    
    sentence = tokenize(sentence)
    x = bag_of_word(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)
    output = model(x)
    _ , pridict = torch.max(output,dim = 1)
    tag = tags[pridict.item()]

    probs = torch.softmax(output,dim = 1)
    prob = probs[0][pridict.item()]

    if prob.item() > .75:
        for intent in intents["intents"]:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: Can u please clearify, I do not understand the previous sentence!")