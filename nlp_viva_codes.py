# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:42:16 2022

@author: Vedant Manelkar
"""

#NLP PRACTS


#EXP1: Basic libraries of python
"""
1. NLTK:NLTK is one of the leading platforms for building Python programs that can work with
human language data. It presents a practical introduction to programming for language processing.
NLTK comes with a host of text processing libraries for sentence detection, tokenization,
lemmatization, stemming, parsing, chunking, and POS tagging.
command:pip install nltk
2.Spacy:spaCy is an open-source NLP library in Python. It is designed explicitly for production
usage – it lets you develop applications that process and understand huge volumes of text.
command:pip install spacy
3.Textblob:TextBlob offers a neat API for performing common NLP tasks like part-of-speech
tagging, noun phrase extraction, sentiment analysis, classification, language translation, word
inflection, parsing, n-grams, and WordNet integration.
command:pip install textblob
4.Gensim : Gensim is a Python library designed specifically for “topic modeling, document indexing,
and similarity retrieval with large corpora.” All algorithms in Gensim are memory-independent, w.r.t.,
the corpus size, and hence, it can process input larger than RAM. With intuitive interfaces, Gensim
allows for efficient multicore implementations of popular algorithms, including online Latent
Semantic Analysis (LSA/LSI/SVD), Latent Dirichlet Allocation (LDA), Random Projections (RP),
Hierarchical Dirichlet Process (HDP) or word2vec deep learning.
command:pip install gensim
5.:Pattern is a text processing, web mining, natural language processing, machine learning,
and network analysis tool for Python. It comes with a host of tools for data mining (Google, Twitter,
Wikipedia API, a web crawler, and an HTML DOM parser), NLP (part-of-speech taggers, n-gram
search, sentiment analysis, WordNet), ML (vector space model, clustering, SVM), and network
analysis by graph centrality and visualization.
command:pip install pattern
"""


#EXP2 :Preprocessing of text (stopword removal, stemming,lemmatization and filteration)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#stopwords
example_sent = """This is a sample sentence, showing off the stop words filtration."""
stop_words = set(stopwords.words('english')) 
word_tokens = word_tokenize(example_sent) 
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w) 
print(word_tokens)
print(filtered_sentence)



from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#stemming and lemmatization
ps = PorterStemmer()
lm=WordNetLemmatizer()  
sentence = "Programmers program with programming languages"
words = word_tokenize(sentence)  
for w in words:
    print(w, " : ", ps.stem(w))
    print(w,":",lm.lemmatize(w))
    
#EXP3:Similar to this i.e getting da root word
#EXP4: Vlab on morphemes
#EXP5:Bigrams
#Making bigrams
import nltk
text='Hi how are you? IT deparmen won dance lmao xd IT lmao xd dance op'
nltk_tokens = nltk.word_tokenize(text)  	
bigrams=list(nltk.bigrams(nltk_tokens))

no_bigrams=len(bigrams)
iT_count=text.count('IT')
bg_count = bigrams.count(('IT', 'deparmen'))


# probabily of 'deparmen' given 'IT' P(bigram | IT)
bg_count/iT_count
# probabilty of bigram in text P(some text)
# i.e. pick a bigram at random, what's the probability it's your bigram:
bg_count/no_bigrams    

#EXP6: Vlab on smoothing
#EXP7:POS Tagging
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence7 = """Today morning, Arthur felt very good."""
tokens = nltk.word_tokenize(sentence7)
tagged = nltk.pos_tag(tokens)
print(tagged)

#EXP8: 
#EXP9:WSD 
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
sentence9 = "I went to the bank to deposit money ."
token_sen9=word_tokenize(sentence9)
token_sen9
print(lesk(token_sen9,'bank','n'))

#wordnet flex
for ss in wn.synsets('bank'):
    print(ss,ss.definition())

#EXP10 :Chunking
#exp10 word tokenize
sample_text10="""
Rama killed Ravana to save Sita from Lanka.The legend of the Ramayan is the most popular Indian epic.A lot of movies and serials have already
been shot in several languages here in India based on the Ramayana.
"""

words=nltk.word_tokenize(sample_text10)
  # print(words)
tagged_words=nltk.pos_tag(words)
  # print(tagged_words)
chunkGram=r"""NN: {}"""
chunkParser=nltk.RegexpParser(chunkGram)
chunked=chunkParser.parse(tagged_words)
chunked.draw()