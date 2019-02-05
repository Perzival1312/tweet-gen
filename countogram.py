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
    histogram = {1:[]}
    for word in source:
        flag = False
        for count, words in histogram.items():
            if word in words:
                flag = True
        if flag:
            if (count + 1) not in histogram:
                histogram[count+1] = [word]
                histogram[count].remove(word)
            else:
                histogram[count+1].append(word)
        else:
                histogram[1].append(word)

    to_remove = []
    for count, words in histogram.items():
        if len(words) == 0:
            to_remove.append(count)
    for index in to_remove:
        histogram.pop(index)
    return histogram

histogram = make_histogram(words_list)
print(histogram)
            