import random, sys, input_validation, os
from PyDictionary import PyDictionary

f = open("/usr/share/dict/words", "r")
words_list = f.readlines()
f.close()
cont = True
dictionary = PyDictionary()

while cont:
    usable = True
    while usable:
        word = random.choice(words_list).strip()
        sys.stdout = open(os.devnull, "w")
        definition = dictionary.meaning(word)
        sys.stdout = sys.__stdout__
        if type(definition) == dict:
            print(dictionary.meaning(word))
            usable = False
        else:
            usable = True

    guess = input("what is the word?\n")
    if guess == word:
        print("congratulations you are correct!")
    else:
        print("that is incorrect, it was {}".format(word))
    cont = input_validation.continuation("Play again?(y/n)")
