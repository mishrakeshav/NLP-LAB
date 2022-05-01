"""
Aim : Word Sense Disambiguation 
"""

from nltk.corpus import wordnet 

input_word = input()

for synonym in wordnet.synsets(input_word):
    print(synonym)
    print(synonym.definition())
    print(synonym.examples())