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

histogram = {}
for words in words_list:
    if words in histogram:
        histogram[words] += 1
    else:
        histogram[words] = 1

times = int(sys.argv[2:3][0])
total = 0
sampling = {}
for key, value in histogram.items():
    total += value
old_key = ""
for key, value in histogram.items():
    if old_key:
        histogram[key] = (value/total)+histogram[old_key]
    else:
        histogram[key] = value/total
    old_key = key

def sample():
    chance = random.random()
    old_key = ""
    choice = ""
    for key, value in histogram.items():
        if old_key:
            if chance < value and chance > histogram[old_key]:
                choice = key
        else:
            if chance < value:
                choice = key
        old_key = key
    return choice

for _ in range(times):
    word = sample()
    if word in sampling:
        sampling[word] += 1
    else:
        sampling[word] = 1

print(sampling)


