# {word: count}
# {word: [count, {next words}]}
# {word: [count, {words: count, words: count, words: count}], total}
# {word: [count, {words: [count, {word: count}, total]}, total]}

import sys, string, random
string.punctuation += "”“’‘—"
string.punctuation += string.digits
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

histogram = {}
words_list = []
table = str.maketrans({key: None for key in string.punctuation})

for strings in word_list:
    words_list += strings.split()
for word in range(len(words_list)):
    words_list[word] = words_list[word].translate(table).lower()
print(len(words_list))

for ind, word in enumerate(words_list):
    if word in histogram:
        histogram[word][0] += 1
        try:
            if words_list[ind + 1] in histogram[word][1]:
                histogram[word][1][words_list[ind + 1]] += 1
                histogram[word][2] += 1
            else:
                histogram[word][1][words_list[ind + 1]] = 1
                histogram[word][2] += 1
        except:
            pass
    else:
        histogram[word] = [1, {}]
        try: 
            histogram[word][1][words_list[ind + 1]] = 1
            histogram[word].append(1)
        except:
            pass

times = int(sys.argv[3:4][0])
total = 0 
sampling = {}

for l in histogram.values():
    total += l[0]

# changes frquency to range of probability of picking key
prev_val = 0
for key, value in histogram.items():
    histogram[key][0] = (value[0]/total)+prev_val
    prev_val = histogram[key][0]
    prev_next_val = 0
    for key_next, value_next in value[1].items():
        value[1][key_next] = value_next/value[2]+prev_next_val
        prev_next_val = value[1][key_next]

'''
    its going to take a word as third arg which will be the first word in the sentence
                    a number as fourth arg which will be the sentnce length
    LOOP:
        random sample of second word - get random word from inset dict
            that word is in first layer
                then get random from that words inset dict
    TODO:
        possibly make a third lvl of dicts
'''

random_sent = [str(sys.argv[2:3][0])]

# gets a random word based on frequency range
def sample():
    prev_word = random_sent[len(random_sent)-1]
    chance = random.random()
    prev_val = 0
    choice = ""
    for key, value in histogram[prev_word][1].items():
        if chance < value and chance > prev_val:
            choice = key
        prev_val = histogram[prev_word][1][key]
    return choice

for _ in range(times):
    random_sent.append(sample())

print(" ".join(random_sent))