"""
Experiment 5:
Aim : TO implement bigrams 
Objective: To understand the N-gram Module
Outcome: Able to implement bigrams from a given corpus and calculate probability of
a sentence.
"""

from nltk.tokenize import word_tokenize 
from collections import Counter
lines = open('sample.txt').read()

tokens = word_tokenize(lines)
tokens = [token.lower() for token in tokens]

def calc_probability(tokens,sentence):
    sentence = word_tokenize(sentence)
    sentence = [word.lower() for word in sentence]

    unigrams = Counter(tokens)
    bigrams = Counter(zip(tokens,tokens[1:]))
    
    output_probability = 1
    for word1,word2 in zip(sentence, sentence[1:]):
        if bigrams[(word1,word2)] == 0 or unigrams[word1] == 0:
            return 0 
        p = bigrams[(word1,word2)] / unigrams[word1]
        output_probability *= p 
    
    return output_probability

print(calc_probability(tokens, 'A database usually structures'))