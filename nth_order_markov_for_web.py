from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, string, utility, random, json

# {(START, word1) : [word2, count]}
# {(word1, word2) : [word3, count]}
# {(word2, word3) : STOPS}

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""
    def __init__(self, source=None, order=2):
        words_list = source
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        self.random_sent = ["START"]
        self.order = order
        self.original_order = order
        for ind, word in enumerate(words_list):
            word_set = [word]
            try:
                for i in range(1, self.order-1):
                    word_set.append(words_list[ind + i])
            except IndexError:
                if self.order == 1:
                    pass
                else:
                    self.order -= 1
                    continue                
            word_set = ' '.join(word_set)
            if (word_set) in self:
                try:
                    if words_list[ind+self.order-1] in self[word_set]:
                        # in first and inset
                        self[word_set][0][words_list[ind+self.order-1]] += 1
                    else:
                        # in first but not inset
                        self[word_set][0][words_list[ind+self.order-1]] = 1
                    self[word_set][1] += 1
                except IndexError:
                    pass
            else:
                try:
                    # new word
                    self[word_set] = [{}, 1]
                    self[word_set][0][words_list[ind+self.order-1]] =  1
                except IndexError:
                    pass
        self.order = self.original_order
    
    @classmethod
    def from_dict(cls, old_dict):
        obj = cls.__new__(cls)
        for key, value in old_dict.items():
            if key.startswith('START'):
                ord = len(key.split())
            obj[key] = value
        obj.order = ord+1
        obj.random_sent = ['START']
        cls.create_random_seed(obj)
        return obj

    def create_random_seed(self):
        possibilies = []
        for key in self.keys():
            key = key.split()
            if key[0] == "START":
                possibilies.append(key)
        self.random_sent = list(random.choice(possibilies))
    
    def count_to_possibility(self):
        for values in self.values():
            prev_val = 0
            for key, value in values[0].items():
                values[0][key] = value/values[1]+prev_val
                prev_val = values[0][key]

    def sample(self):
        prev_word = []
        for i in range(self.order-1, 0, -1):
            prev_word.append(self.random_sent[len(self.random_sent)-i])
        prev_word = ' '.join(prev_word)
        chance = random.random()
        prev_val = 0
        choice = ""
        for key, value in self[prev_word][0].items():
            if chance < value and chance > prev_val:
                choice = key
                break
            prev_val = self[prev_word][0][key]
        return choice

    def get_sentence(self):
        self.create_random_seed()
        try:
            next = ""
            while next != "STOP":
                next = self.sample()
                if next != "START":
                    self.random_sent.append(next)
        except KeyError:
            self.get_sentence()
        except RecursionError:
            pass
        try:
            sentence = " ".join(self.random_sent[1:len(self.random_sent)-1])
            return sentence[0].capitalize() + sentence[1:] + '.'
        except IndexError:
            self.random_sent = ['START']
            self.get_sentence()
