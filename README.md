# Chatbot with Neural Network

## Description
A simple chatbot implementation using PyTorch neural networks with both command-line and GUI interfaces.

## Features
- Neural network-based response generation
- Command-line interface
- Graphical user interface using Tkinter
- Configurable through intents.json
- Natural language processing using NLTK

## Requirements
- Python 3.x
- PyTorch
- NLTK
- Tkinter (included with Python)

## Installation
1. Clone the repository
2. Install required packages:
3. Download the required NLTK data:

pip install torch nltk numpy


## Project Structure

- `training.ipynb` - Jupyter notebook containing the model training process
- `model.py` - Neural network model definition
- `Utils.py` - Utility functions for text processing
- `chatbot.py` - Core chatbot implementation
- `GUI.py` - Graphical user interface
- `intents.json` - Training data and response patterns
- `data.pth` - Trained model weights and configuration

## Usage

### GUI Version
Run the chatbot with graphical interface:

python GUI.py

### Command-line Version
Run the chatbot in command-line mode:

python chatbot.py


## How It Works

1. **Text Processing**: User input is tokenized and stemmed using NLTK
2. **Intent Classification**: Processed text is fed into a neural network
3. **Response Generation**: Bot selects appropriate response based on classified intent
4. **Confidence Check**: Responses are only given if confidence exceeds 75%

## Model Architecture

- Input Layer: Based on bag-of-words size
- Hidden Layer: Configurable size (default: 8 neurons)
- Output Layer: Number of possible intents
- Activation Function: ReLU

## Training

The model is trained using:
- Cross Entropy Loss
- Adam Optimizer
- Batch Size: 8
- Learning Rate: 0.001
- Epochs: 1000

## Customization

You can customize the chatbot's responses by modifying the `intents.json` file. The file structure should follow this format:
json
{
"intents": [
{
"tag": "greeting",
"patterns": ["Hello", "Hi", "Hey"],
"responses": ["Hi there!", "Hello!", "Hey!"]
}
]
}

## License

This project is open source and available under the MIT License.

