from dictogram_official import Dictogram
import sys

word_list = []
f = open(str(sys.argv[1:2][0]), 'r')
texts_list = f.readlines()
f.close()

try:
    for text in texts_list:
        g = open(text.strip(), 'r')
        word_list += g.readlines()
        g.close()
except:
    print(text)
    word_list = texts_list

histogram = Dictogram(word_list)
print(histogram['the'])