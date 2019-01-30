import sys

f = open(str(sys.argv[1:][0]), 'r')
word_list = f.readlines()
f.close()

histogram = {}
words_list = []

for strings in word_list:
    words_list += strings.split()

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

histogram = make_histogram(words_list)
print(unique_words(histogram))
