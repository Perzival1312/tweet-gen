import string

string.punctuation += "”“’‘—"
string.punctuation += string.digits

def cleanse(text):
    table = str.maketrans({key: None for key in string.punctuation})
    words_list = []
    for strings in text:
        words_list += strings.split()
    for word in range(len(words_list)):
        words_list[word] = words_list[word].translate(table).lower()
    return words_list

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
        print(repr(text), "not a file")
        word_list = texts_list
    return word_list
