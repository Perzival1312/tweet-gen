import sys

f = open(str(sys.argv[1:][0]), 'r')
word_list = f.readlines()
f.close()

histogram = {}
words_list = []

for strings in word_list:
    words_list += strings.split()

for words in words_list:
    if words in histogram:
        histogram[words] += 1
    else:
        histogram[words] = 1

print(histogram['Frankenstein'])
