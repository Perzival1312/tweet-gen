import sys, string
string.punctuation += "”“’‘—"

# f = open(str(sys.argv[1:][0]), 'r')
f = open('fishes.txt', 'r')
word_list = f.readlines()
f.close()

histogram = []
words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()

def make_histogram(source):
    histogram = []
    for words in source:
        count = source.count(words)
        # equalivent to
        # count = 0
        # for checking in source:
        #     if words == checking:
        #         count += 1
        histogram.append((words, count))
    return list(set(histogram))

def make_histogram_2(source):
    histogram = [('test', [0])]
    for word in source:
        for wtuple in histogram:
            if wtuple[0] == words_list:
                print(wtuple[1][:])# += 1
                wtuple[1][:] += 1
            else:
                histogram.append((word, [1]))
        # else:
        #     histogram.append((word, [1]))
    return histogram

histogram = make_histogram_2(words_list)
print(histogram)