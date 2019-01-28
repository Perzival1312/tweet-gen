import random, sys
str_input = sys.argv[1:]
shuffled = []
for i in range(len(str_input)):
    choice = random.choice(str_input)
    shuffled.append(choice)
    str_input.remove(choice)
print(shuffled)