import random, sys
str_input = sys.argv[1:]

# shuffled = []

# rand_ints = random.sample(range(0, len(str_input)), len(str_input))
# for indexes in rand_ints:
#     shuffled.append(str_input[indexes])

# for i in range(len(str_input)):
#     choice = random.choice(str_input)
#     shuffled.append(choice)
#     str_input.remove(choice)

# print(shuffled)

# for index, value in enumerate(str_input):
#     choice = random.choice(str_input)
#     choice_index = str_input.index(choice)
#     temp = value
#     str_input[index] = choice
#     str_input[choice_index] = temp
# print(str_input)

anagrams = []
for words in str_input:
    word_ana = []
    fin_word_ana = []
    for letter in range(len(words)):
        word_ana += words[letter:letter+1]
    rand_indexes = random.sample(range(0, len(word_ana)), len(word_ana))
    for indexes in rand_indexes:
        fin_word_ana.append(word_ana[indexes])
    anagrams.append("".join(fin_word_ana))
print(" ".join(anagrams))


