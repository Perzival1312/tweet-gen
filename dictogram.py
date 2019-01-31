import sys, string
string.punctuation += "”“’‘—"

f = open(str(sys.argv[1:][0]), 'r')
word_list = f.readlines()
f.close()

histogram = {}
words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()

def make_histogram(source):
    histogram = {}
    for words in source:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1
    return histogram

def unique_words(histogram):
    unique_word_counter = 0
    for values in histogram.items():
        if values == 1:
            unique_word_counter += 1
    return unique_word_counter

def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return("word is not in source text")

histogram = make_histogram(words_list)
unique_words(histogram)
frequency('the', histogram)