import random, sys
f = open('/usr/share/dict/words', 'r')
words_list = f.readlines()
f.close()
word_count = sys.argv[1:]
final_words = []
try:
    int(word_count)
    for _ in range(int(word_count[0])):
        final_words.append(random.choice(words_list)) 
except:
    word_fragment = word_count[0]
    for words in words_list:
        temp_word = words[:len(word_fragment)]
        if temp_word == word_fragment:
            final_words.append(words)
print("".join(final_words))