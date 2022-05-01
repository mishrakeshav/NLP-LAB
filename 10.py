from nltk.tokenize import word_tokenize
lines = open('sample.txt').read()
tokens = word_tokenize(lines)
tokens = [token.lower() for token in tokens]

BAD_CHARS = [';', ':', '!', "*", '<', '>','#','?','@','p',',','.','(',')']
no_bad_chars = list(filter(lambda token: token not in BAD_CHARS, tokens))

from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))
no_stop_words = list(filter(lambda token: token not in STOP_WORDS, no_bad_chars))

from nltk import pos_tag
pos_tags = list(pos_tag(no_stop_words))


from nltk import RegexpParser
"""
NP - Noun Phrase 
NN - Noun 
IN - Preposition 
V - Verb 
PP - Preposition Phrase 
VP : Verb Phrase 
JJ - Adjective 
"""
chunker = RegexpParser("""
    NP: {<DT>?<JJ>*<NN>}
    P: {<IN>}
    V: {<V>.*}
    PP: {<P> <NP>}
    VP: {<V> <NP|PP>*}
""")

  
output = chunker.parse(pos_tags)
output.draw()
#print(output)