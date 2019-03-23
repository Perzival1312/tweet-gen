from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, string, utility, random, json

# {(START, word1) : [word2, count]}
# {(word1, word2) : [word3, count]}
# {(word2, word3) : STOPS}

class Markov(dict):
    """Markov is a histogram implemented as a subclass of the dict type."""
    def __init__(self, source=None, order=1):
        if order < 1:
            raise ValueError('Order needs to be greater than or equal to 1.')
        words_list = source
        super(Markov, self).__init__()  # Initialize this as a new dict
        self.random_sent = ["START"]
        self.order = order
        init_window_size = order 
        # Creates a set of words the number of which is the Order to act as the key
        for ind, word in enumerate(words_list):
            word_set = [word]
            try:
                for i in range(1, init_window_size):
                    word_set.append(words_list[ind + i])
            # towards end of input and window size should shrink so as not to get index errors
            except IndexError:
                if init_window_size == 0:
                    pass
                else:
                    init_window_size -= 1
                    continue                
            word_set = ' '.join(word_set)
            # Adds new words to the dict depending on whether or not they are already inside
            if (word_set) in self:
                try:
                    if words_list[ind+init_window_size] in self[word_set]:
                        # in first and inset
                        self[word_set][0][words_list[ind+init_window_size]] += 1
                    else:
                        # in first but not inset
                        self[word_set][0][words_list[ind+init_window_size]] = 1
                    self[word_set][1] += 1
                except IndexError:
                    pass
            else:
                try:
                    # new word
                    self[word_set] = [{}, 1]
                    self[word_set][0][words_list[ind+init_window_size]] =  1
                except IndexError:
                    pass
    
    @classmethod
    def from_dict(cls, old_dict):
        '''Creates new Markov object from a given dictionary represention of a Markov'''
        markov = cls.__new__(cls)
        for word_set, hist_tokens in old_dict.items():
            if word_set.startswith('START'):
                order = len(word_set.split())
            markov[word_set] = hist_tokens
        markov.order = order
        markov.random_sent = ['START']
        cls.create_random_seed(markov)
        return markov

    def create_random_seed(self):
        '''gets the first set of words to start the randomly generated sentence'''
        possibilies = []
        for key in self.keys():
            key = key.split()
            if key[0] == "START":
                possibilies.append(key)
        self.random_sent = list(random.choice(possibilies))
    
    def count_to_possibility(self):
        '''generate cumulative probabilities'''
        for values in self.values():
            prev_val = 0
            for key, value in values[0].items():
                values[0][key] = value/values[1]+prev_val
                prev_val = values[0][key]

    def sample(self):
        '''gets the next word based on the previous set of words'''
        prev_words = []
        for i in range(self.order, 0, -1):
            prev_words.append(self.random_sent[len(self.random_sent)-i])
        prev_words = ' '.join(prev_words)
        chance = random.random()
        prev_val = 0
        choice = ""
        for key, value in self[prev_words][0].items():
            if chance < value and chance > prev_val:
                choice = key
                break
            prev_val = self[prev_words][0][key]
        return choice

    def get_sentence(self):
        '''generates the sentence using sample() to get next'''
        self.create_random_seed()
        next = ""
        while next != "STOP":
            next = self.sample()
            if next != "START" and next != '':
                self.random_sent.append(next)
        # formats sentence for mass consumption
        sentence = " ".join(self.random_sent[1:len(self.random_sent)-1])
        # remove spaces before punctuation 
        for ind, character in enumerate(sentence):
            if character == ' ':
                if ind+1 < len(sentence):
                    if string.punctuation.__contains__(sentence[ind+1]):
                        sentence = sentence[:ind] + sentence[ind+1:]
        return sentence[0].capitalize() + sentence[1:] + '.'


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) == 2:
        words = utility.read(arguments[0])
        words = utility.cleanse(words)
        histogram = Markov(words, int(arguments[1]))
        histogram.count_to_possibility()
        print(histogram.get_sentence())

if __name__ == '__main__':
    main()
