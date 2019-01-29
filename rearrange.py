import random, sys
str_input = sys.argv[1:]

shuffled = []

rand_ints = random.sample(range(0, len(str_input)), len(str_input))
for indexes in rand_ints:
    shuffled.append(str_input[indexes])

# for i in range(len(str_input)):
#     choice = random.choice(str_input)
#     shuffled.append(choice)
#     str_input.remove(choice)

print(shuffled)

# for index, value in enumerate(str_input):
#     choice = random.choice(str_input)
#     choice_index = str_input.index(choice)
#     temp = value
#     str_input[index] = choice
#     str_input[choice_index] = temp
# print(str_input)


