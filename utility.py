import string, os, re

import nltk, pprint
from nltk.corpus import PlaintextCorpusReader
nltk.download('punkt')

def cleanse(text):
    '''Cleans and tokenizes input text'''
    # turn text into one long string
    # remove everything before the important text
    # remove everything after the important text
    # add start and stop tokens
    # turn into array of individual words
    text = ' '.join(text)
    text = re.sub(r'(.|\n)*(\*{2,3}[ ]?(START OF).*(\n)?.*\*{2,3})', "", text, count=1)
    text = re.sub(r'(\*{2,3}[ ]?(END OF).*(\n)?.*\*{2,3})(.|\n)*', "", text, count=1)
    sents = nltk.sent_tokenize(text)
    for ind, sentences in enumerate(sents):
        sents[ind] = 'START ' + sentences[:len(sentences)-1] + ' STOP'
    # not the best way of doing it but works
    words = ' '.join(sents).split()
    return words

def read(source):
    texts_list, word_list = [], []
    f = open(source, 'r')
    texts_list = f.readlines()
    f.close()
    try:
        for text in texts_list:
            g = open(text.strip(), 'r')
            word_list += g.readlines()
            g.close()
    except:
        # print(repr(text), "is not a file")
        word_list = texts_list
    return word_list
