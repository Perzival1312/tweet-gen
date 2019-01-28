import random, sys
str_input = sys.argv[1:]
# shuffled = []
# for i in range(len(str_input)):
#     choice = random.choice(str_input)
#     shuffled.append(choice)
#     str_input.remove(choice)
# print(shuffled)

length = len(str_input)
for index, value in enumerate(str_input):
    choice = random.choice(str_input)
    choice_index = str_input.index(choice)
    temp = value
    str_input[index] = choice
    str_input[choice_index] = temp
print(str_input)
    


# random.randrange(len(words_list))[:-1]