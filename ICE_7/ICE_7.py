import nltk
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import trigrams as tr

# Loading the text file
TEXT = file('input.txt').read()  # To read the entire text file at a time, here the entire paragraph
print(TEXT)
#Tokenization
L = word_tokenize(TEXT)
print L
#WordNet
for i in L:
    synsets = wn.synsets(i)
    print [str(syns.definition) for syns in synsets]
#Stemming
for i in L:
    stemmer=PorterStemmer()
    stemmer.stem(i)
    print stemmer.stem(i)
#Parts of Speech
print pos_tag(L)
#Lemmatization
for i in L:
    lemmatizer=WordNetLemmatizer()
    lemmatizer.lemmatize(i)
    print lemmatizer.lemmatize(i)
#Trigram
print(nltk.trigrams(L))  # Trigram command
#Named Entity Recognition
print ne_chunk(pos_tag(L))
