import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

# Read the whole text file one at a time
TEXT = file('textfile.txt').read()
print(TEXT)
#Start the Tokenization
words = word_tokenize(TEXT)
print words
lemmatizedWord= []
#applying lemmatization on the tokenized word
for i in words:
   lemmatizer = WordNetLemmatizer()
   lemmatized = lemmatizer.lemmatize(i.lower())
   lemmatizedWord.append(lemmatized)

print "\nThe lemmatized words are:"
print(lemmatizedWord)

# Using POS tagging to identify verbs
apply_POS = pos_tag(lemmatizedWord)
print "\n removing verbs:"
print apply_POS
#sent=pos_tag(words)
verb_remove=[s for s in apply_POS if s[1] != 'VB'and 'VBD'and'VBG'and'VBN'and'VBP'and'VBZ'and'.'and','and'?'and'!']
print "\nAfter Removing of the  verbs:"
print verb_remove
#calculating  repeated words top 5
freg_apply = nltk.FreqDist(lemmatizedWord)
top_five = freg_apply.most_common(5)
print("\n Top five words")
print(top_five)
#selection of the sentence containing the top five words
sent_TEXT = sent_tokenize(TEXT) #tokenize the sentence in the text document
repeat_sent = []

for sent in sent_TEXT:
  for word in word_tokenize(sent):

    for (k, l) in top_five:
       if word == k:
           repeat_sent.append(sent)
#print the sentence which contain top five words
print ("\n Sentences which contain top five words")
print(repeat_sent)