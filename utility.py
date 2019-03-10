import string, os
end_punt = ".!?"
string.punctuation += "”“’‘—"
string.punctuation += string.digits
period_str = "\nSTOP\nSTART"

def cleanse(text):
    ret_list = []
    words_list = []
    periods = str.maketrans({key: period_str for key in end_punt})
    other_punct = str.maketrans({key: None for key in string.punctuation})
    if(os.environ['SETTINGS'] == 'DevelopmentConfig'):
        for sentences in text:
            words_list += sentences.split()
    if(os.environ['SETTINGS'] == 'ProductionConfig'):
        words_list = text.split()
    # for sentences in text:
    #     words_list += sentences.split()
    
    for word in range(len(words_list)):
        if words_list[word] != 'I' or words_list[word] != 'i':
            words_list[word] = words_list[word].lower()
    for word in range(len(words_list)-1):
        words_list[word] = words_list[word].translate(periods)
    for word in range(len(words_list)):
        words_list[word] = words_list[word].translate(other_punct).splitlines()
    for word in words_list:
        ret_list.extend(word)
    ret_list.insert(0, "START")
    ret_list.append("STOP")
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
    return word_list
