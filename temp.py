# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#run the next two commands to download all required files

#import nltk
#nltk.download()

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#Tokenize on sentence
print(sent_tokenize(EXAMPLE_TEXT))

#Tokenize on word
print(word_tokenize(EXAMPLE_TEXT))

#Use English stop words
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(EXAMPLE_TEXT)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))
    
new_text = "Generally pythoners use python but they never catch a python for fear of pythoned."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))