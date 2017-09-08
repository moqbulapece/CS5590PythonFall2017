import re
# import the regular expression module
file_text = 'textfile.txt'
# textfile.txt is the file which contains the paragraph

list_word = re.split('\s+', file(file_text).read().lower())#read the file and split the words in lower case
print 'Total Words in file:', len(list_word)
# the  dictionary which will contains teh pairs of word:frequency
target_dictionary = {}

for word in list_word:
    if word in target_dictionary:

        target_dictionary[word] += 1 #if the same word in the dictionary repeated add 1
    else:
        target_dictionary[word] = 1 #if the word is unique it will be count as 1

print 'The Unique words:', len(target_dictionary)#calculation of the number of unique words
print target_dictionary #print the dictionary which cantins the frequency of words
