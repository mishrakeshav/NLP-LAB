from nltk.corpus import wordnet,stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 

BAD_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '.', ',', '?', '/']
STOP_WORDS = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def preprocess(lines):
    tokens = word_tokenize(lines)
    tokens = [token.lower() for token in tokens]
    
    no_bad_chars = list(filter(lambda token: token not in BAD_CHARS, tokens))
    no_stop_words = list(filter(lambda token: token not in STOP_WORDS, no_bad_chars))
    
    return no_stop_words

def get_word_lemmas(tokens):
    word_lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return word_lemmas

def get_synonyms_lemma(word):
    synonyms = []

    for synonym in wordnet.synsets(word):
        synonyms += [lemma.name() for lemma in synonym.lemmas()]

    return synonyms

def get_word_and_syn_lemmas(tokens):
    word_and_syn_lemmas = []    # Should contain the lemma of the word and its synonyms

    for word in tokens:
        word_and_syn_lemmas.append(lemmatizer.lemmatize(word))   # Adding the lemma of the word
        word_and_syn_lemmas.extend(get_synonyms_lemma(word))     # Adding the lemma of all the synonyms of the word
    
    return word_and_syn_lemmas

def words_simlilarity_score(word1, word2):
    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)
        return w1.wup_similarity(w2)
    except:
        return 0

query_sentence = "Will be given by the user"
file_1 = open('cricketbat.txt').read() 
file_2 = open('vampirebat.txt').read()

tokens1 = preprocess(file_1) 
tokens2 = preprocess(file_2) 
tokens3 = preprocess(query_sentence)


word_lemmas_1 = get_word_lemmas(tokens1)
word_syn_lemmas_1 = get_word_and_syn_lemmas(tokens1)

word_lemmas_2 = get_word_lemmas(tokens2)
word_syn_lemmas_2 = get_word_and_syn_lemmas(tokens2)

word_lemmas_3 = get_word_lemmas(tokens3)
word_syn_lemmas_3 = get_word_and_syn_lemmas(tokens3)

exact_word_match13 = 0
exact_word_match23 = 0
for word3 in word_lemmas_3:
    for word1 in word_lemmas_1:
        exact_word_match13 += 1 if word1 == word3 else 0

    for word2 in word_lemmas_2:
        exact_word_match23 += 1 if word2 == word3 else 0

similarity_score13 = 0
similarity_score23 = 0
for word3 in word_lemmas_3:
    for word1 in word_lemmas_1:
        similarity_score13 += words_simlilarity_score(word3, word1)

    for word2 in word_lemmas_2:
        similarity_score23 += words_simlilarity_score(word3, word2)

file1_score = exact_word_match13 + similarity_score13
file2_score = exact_word_match23 + similarity_score23

if file1_score > file2_score: print("The query sentence belongs to file1")
else: print("The query sentence belongs to file2")