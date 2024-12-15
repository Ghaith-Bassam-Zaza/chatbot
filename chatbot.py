from model import NeuralNet
import random
import torch
from json import load
from Utils import bag_of_word, tokenize

# get device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# load dataset
with open("./intents.json") as f:
    intents = load(f)

# load model
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

# create bot
bot_name = "Foulan"
print("Let's chat! type 'quit' to exit.")
def get_bot_response(sentence):
    # pre-process input then push it into the model
    sentence = tokenize(sentence)
    x = bag_of_word(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)
    output = model(x)

    # get output tag with probability
    _ , pridict = torch.max(output,dim = 1)
    tag = tags[pridict.item()]
    probs = torch.softmax(output,dim = 1)
    prob = probs[0][pridict.item()]

    # if probability is high for a tag give a random answer from the tag answers, else ask user to clearify
    if prob.item() > .75:
        for intent in intents["intents"]:
            if tag == intent['tag']:
                return f"{bot_name}: {random.choice(intent['responses'])}"
    else:
        return f"{bot_name}: Can u please clearify, I do not understand the previous sentence!"

if __name__ == "__main__":
    # bot loop
    while True:
        sentence = input("You: ")
        # end loop
        if sentence == "quit":
            break
        print(get_bot_response(sentence))