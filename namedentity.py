# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:20:26 2015

@author: nilakant
"""


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
#unsupervised tokenizer
train_text = state_union.raw("2006-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
            
            #print(tagged)
            
    except Exception as e:
        print(str(e))
        
process_content()