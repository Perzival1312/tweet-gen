import string, os, re
end_punt = ".!?"
string.punctuation += "”“’‘—"
string.punctuation += string.digits
apostophe_ind = string.punctuation.index("'")
string.punctuation = string.punctuation[:apostophe_ind] + string.punctuation[apostophe_ind+1:]
print(string.punctuation)
period_str = "\nSTOP\nSTART"

def cleanse(text):
    ret_list = []
    words_list = []
    periods = str.maketrans({key: period_str for key in end_punt})
    other_punct = str.maketrans({key: None for key in string.punctuation})
    text = ' '.join(text)
    text = re.sub(r'(.|\n)*(\*{2,3}[ ]?(START OF).*(\n)?.*\*{2,3})', "", text, count=1) 
    text = re.sub(r'(\*{2,3}[ ]?(END OF).*(\n)?.*\*{2,3})(.|\n)*', "", text, count=1) 
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
    # print(repr(ret_list[:250]))
    # print(repr(ret_list[169]))

    # for i in range(50):
    #     print(ret_list[i])
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
