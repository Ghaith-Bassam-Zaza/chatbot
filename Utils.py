from nltk import word_tokenize
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
import numpy as np
def tokenize(sentense):
    return word_tokenize(sentense)

stemmer = PorterStemmer()
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_word(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]=1.0

            
    return bag