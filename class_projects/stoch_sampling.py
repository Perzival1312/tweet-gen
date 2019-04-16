import string, sys, random

string.punctuation += "”“’‘—"

f = open(str(sys.argv[1:2][0]), "r")
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

try:
    times = int(sys.argv[2:3][0])
except IndexError:
    times = 1000

letter_value = "0" + string.ascii_lowercase
# total = sum(histogram.values())
sampling = {}


def get_weighted_total():
    total = 0
    for key, value in histogram.items():
        total += letter_value.index(key[0])
        total += value
    return total


total = get_weighted_total()
print(total)

# changes frquency to range of probability of picking key
prev_val = 0
for key, value in histogram.items():
    histogram[key] = ((value + letter_value.index(key[0])) / total) + prev_val
    prev_val = histogram[key]

# gets a random word based on frequency range
def sample():
    chance = random.random()
    prev_val = 0
    choice = ""
    for key, value in histogram.items():
        if chance < value and chance > prev_val:
            choice = key
        prev_val = histogram[key]
    return choice


for _ in range(times):
    word = sample()
    if word in sampling:
        sampling[word] += 1
    else:
        sampling[word] = 1

print(histogram)
print(sampling)
print(letter_value.index("a"))
