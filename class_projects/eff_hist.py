import sys, string

string.punctuation += "”“’‘—"

f = open(str(sys.argv[1:][0]), "r")
word_list = f.readlines()
f.close()

histogram = {}
words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()

for words in words_list:
    if words in histogram:
        histogram[words] += 1
    else:
        histogram[words] = 1

counts = histogram.values()
eff_hist = [[] for _ in range((max(counts) + 1))]
fin_hist = []
l = []

for word, count in histogram.items():
    eff_hist[count].append(word)

for index, lists in enumerate(eff_hist):
    fin_hist.append((index, lists))

for tuples in fin_hist:
    if tuples[1]:
        l.append(tuples)
print(l)
