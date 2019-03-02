import string
end_punt = ".!?"
# string.punctuation = string.punctuation[:13]+string.punctuation[14:]
string.punctuation += "”“’‘—"
string.punctuation += string.digits
period_str = "\nSTOP\nSTART"

def cleanse(text):
    # print("text: ", text)
    ret_list = []
    words_list = []
    periods = str.maketrans({key: period_str for key in end_punt})
    other_punct = str.maketrans({key: None for key in string.punctuation})
    # start_stop = str.maketrans({key: period_str for key in "."})
    # print(type(text), text)
    for sentences in text:
        words_list += sentences.split()
    # for strings in text:
    #     words_list.extend(strings)
    # print(words_list)
    for word in range(len(words_list)-1):
        words_list[word] = words_list[word].translate(periods)
    # print(words_list)
    for word in range(len(words_list)):
        words_list[word] = words_list[word].translate(other_punct).splitlines()
    # print(words_list)
    # for word in range(len(words_list)-1):
    #     words_list[word] = words_list[word].translate(start_stop)#.split()
    for word in words_list:
        ret_list.extend(word)
    ret_list.insert(0, "START")
    ret_list.append("STOP")
    # print(ret_list)
    # print(words_list)
    return ret_list

def read(source):
    texts_list, word_list = [], []
    f = open(source, 'r')
    texts_list = f.readlines()
    f.close()
    try:
        for text in texts_list:
            g = open(text.strip(), 'r')
            word_list += g.readlines()
            g.close()
    except:
        # print(repr(text), "is not a file")
        word_list = texts_list
    # ret_list = []
    # for word in word_list:
    #     ret_list.extend(word)
    # print("source: ", word_list)
    return word_list
