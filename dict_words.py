import random, sys
f = open('/usr/share/dict/words', 'r')
words_list = f.readlines()
f.close()
word_count = sys.argv[1:]
final_words = []
for i in range(int(word_count[0])):
    final_words.append(random.choice(words_list))
print("".join(final_words))