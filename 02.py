"""
Experiment 2:
Objective : To understand and learn basic preprocessing of text
Outcome: Able to implement preprocessing of text as tokenization, stop word removal, stemming , lemmatization etc.
"""

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer,WordNetLemmatizer
from tabulate import tabulate

lines = open('sample.txt').read()

tokens = word_tokenize(lines)
tokens = [token.lower() for token in tokens]

print('TOKENS:')
print(tokens)

BAD_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '.', ',', '?', '/']
no_bad_words = list(filter(lambda w : w not in BAD_CHARS, tokens))
print("NO BAD WORDS:")
print(no_bad_words)

STOP_WORDS = stopwords.words('english')
no_stop_words = list(filter(lambda w : w not in STOP_WORDS, no_bad_words))
print("NO STOP WORDS:")
print(no_stop_words)


stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in no_stop_words]


lemmatizer = WordNetLemmatizer()
lemma = [lemmatizer.lemmatize(word) for word in no_stop_words]

print(tabulate(zip(no_stop_words, stems, lemma), headers=['WORD', 'STEM', 'LEMMA']))

