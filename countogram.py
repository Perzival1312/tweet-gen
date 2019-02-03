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


# histogram = {count: {count: [words, words, words]}}
# words = {count: [words, words, words]}
# histogram = {count: [words, words, words]}
# words = [words, words]





def make_histogram(source):
    histogram = {1:[]}
    for word in source:
        for count, words in histogram.items():
            print(repr(count), repr(words), repr(word))
            if word in words:
                print("contains used word")
                if (count + 1) not in histogram:
                    print("in word list without count")
                    print(count)
                    histogram[count+1] = [word]
                    histogram[count].remove(word)
                    break
                else:
                    print("in word list with count")
                    print(count)
                    histogram[count+1].append(word)
                    break
            else:
                print("new word")
                histogram[1].append(word)
                break
        print(repr(histogram), "\n\n\n")
    return histogram
histogram = make_histogram(words_list)
print(histogram)
            