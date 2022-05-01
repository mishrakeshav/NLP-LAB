from nltk import word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords,wordnet 

def preprocess(lines):
    tokens = word_tokenize(lines)
    tokens = [token.lower() for token in tokens]
    BAD_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '.', ',', '?', '/']
    STOP_WORDS = stopwords.words('english')
    no_bad_chars = list(filter(lambda w : w not in BAD_CHARS, tokens))
    no_stop_words = list(filter(lambda w : w not in STOP_WORDS, no_bad_chars))
    return no_stop_words

def get_word_lemmas(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in tokens]

def get_synonym_lemmas(word):
    synonyms = []
    for synonym in wordnet.synsets(word):
        synonyms += [lemma.name() for lemma in synonym.lemmas()]
    return synonyms

def get_word_and_syn_lemmas(tokens):
    word_and_syn_lemmas = []
    lemmatizer = WordNetLemmatizer()
    for word in tokens:
        word_and_syn_lemmas.append(lemmatizer.lemmatize(word))
        word_and_syn_lemmas.extend(get_synonym_lemmas(word))
    return word_and_syn_lemmas


def word_similarity_score(word1,word2):
    word1 = word1 + '.n.01'
    word2 = word2 + '.n.01'
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)
        return w1.wup_similarity(w2)
    except Exception as e:
        print(e)
        return 0 


query_sentence = "virat kohli scored 100 run with his bat"
file_1 = open('cricketbat.txt').read() 
file_2 = open('vampirebat.txt').read()

token1 = preprocess(file_1)
token2 = preprocess(file_2)
token3 = preprocess(query_sentence)


word_lemma_1 = get_word_lemmas(token1)
word_lemma_2 = get_word_lemmas(token2)
word_lemma_3 = get_word_lemmas(token3)

word_syn_lemmas_1 = get_word_and_syn_lemmas(token1)
word_syn_lemmas_2 = get_word_and_syn_lemmas(token2)
word_syn_lemmas_3 = get_word_and_syn_lemmas(token3)

exact_match_word13 = 0 
exact_match_word23 = 0 

for word3 in word_lemma_3:
    for word2 in word_lemma_2:
        if word3 == word2:
            exact_match_word23 += 1 
    
    for word1 in word_lemma_1:
        if word3 == word1:
            exact_match_word13 += 1 
    

similarity_score_13 = 0 
similarity_score_23 = 0

for word3 in word_syn_lemmas_3:
    for word1 in word_syn_lemmas_1:
        similarity_score_13 += word_similarity_score(word3,word1)
    
    for word2 in word_syn_lemmas_2:
        similarity_score_23 += word_similarity_score(word3,word2)

if exact_match_word13 + similarity_score_13 > exact_match_word23 + similarity_score_23:
    print('The Query Sentence belongs to file1')
else:
    print('The Query Sentence belongs to file2')
