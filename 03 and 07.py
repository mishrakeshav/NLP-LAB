"""
Experiment 3:
Objective : To understand morphological features of a word and generation of word forms
Outcome: Able to implement and analyze morphological features of a word and generation of word forms from the root and suffix information

Experiment 7: 
Objective: To understand Part of Speech tagging.
Outcome: Able to implement and Find POS tags of words in a sentence.

"""

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk.stem import WordNetLemmatizer 
from tabulate import tabulate
from nltk import pos_tag 

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

postags = list(pos_tag(no_stop_words))


word,tags = zip(*postags)
print(tabulate(zip(no_stop_words, stems, lemma, tags), headers=['WORD', 'STEM', 'LEMMA', 'TAGS']))