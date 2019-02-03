import string, sys, random
string.punctuation += "”“’‘—"

f = open(str(sys.argv[1:2][0]), 'r')
word_list = f.readlines()
f.close()

words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()

histogram = []
for j in range(len(words_list)):
    contains = False
    if len(histogram) == 0:
        histogram.append([words_list[j], 1])
    else:
        for i in range(len(histogram)):
            if words_list[j] == histogram[i][0]:
                histogram[i][1] += 1
                contains = True
        if not contains:
            histogram.append([words_list[j], 1])

times = int(sys.argv[2:3][0])
total = 0
sampling = []

for sets in histogram:
    total += sets[1]
for index, sets in enumerate(histogram):
    if index-1 >= 0:
        sets[1] = (sets[1]/total) + histogram[index-1][1]
    else:
        sets[1] = sets[1]/total

def sample():
    chance = random.random()
    choice = ""
    for index, sets in enumerate(histogram):
        if index-1 >= 0:
            if chance < sets[1] and chance > histogram[index-1][1]:
                choice = sets[0]
        else:
            if chance < sets[1]:
                choice = sets[0]
    return choice

for _ in range(times):
    selected = sample()
    contains = False
    if len(sampling) == 0:
        sampling.append([selected, 1])
    else:
        for i in range(len(sampling)):
            if selected == sampling[i][0]:
                sampling[i][1] += 1
                contains = True
        if not contains:
            sampling.append([selected, 1])

print(histogram)
print(sampling)
