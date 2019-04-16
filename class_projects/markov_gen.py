from dictogram_official import Dictogram
import sys, utility

word_list = []
source = str(sys.argv[1:2][0])
word_list = utility.read(source)
word_list = utility.cleanse(word_list)

histogram = Dictogram(word_list)
print(histogram["the"])
