# PNlCoe XpoqFe
""" HTML class for defs only need the first
add to array use arr[0]
from 'define {word}'
"""
import requests, random
from bs4 import BeautifulSoup
f = open('/usr/share/dict/words', 'r')
words_list = f.readlines()
f.close()
not_right = True
while not_right:
    word = random.choice(words_list)
    word = 'homocercal'
    print(word)
    url = 'https://www.google.com/search?q=define+{}'.format(word)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")
    soup = soup.find('span', {"class": "st"})
    # print(soup)
    soup = str(soup)
    # print(len(soup))
    if soup.find(word.capitalize()) != -1:
        if len(soup) > 1:
            soup = soup[soup.find('<b>{}</b>'.format(word.capitalize())):]#:soup.find('.')]
        # print(soup)
    else:
        if len(soup) > 1:
            soup = soup[soup.find('<b>{}</b>'.format(word)):]#:soup.find('.')]
        # print(soup)
    print(len(soup), soup)
    if len(soup)>0:
        not_right = False
# print(soup.find('span', {"class": "st"}))
