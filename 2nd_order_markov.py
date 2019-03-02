from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, string, utility, random

# {word: count}
# {word: [{next words}, total]}
# {word: [{words: count, words: count, words: count}], total}
# {word: [{words: [count, {word: count}, total]}, total]}


# {START: [{word1: [count, {word2: count}, total]}, total]}
# {word1: [{word2: [count, {word3: count}, total]}, total]}
# {word2: [{word3: [count, {STOP: count}, total]}, total]}

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, source=None):
        words_list = source
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.random_sent = ["START"]
        # Count words in given list, if any
        # if words_list is not None:
        #     for word in words_list:
        #         self.add_count(word)

        for ind, word in enumerate(words_list):
            # print(word, words_list[ind+1], words_list[ind+2])
            if word in self:
                try:
                    if words_list[ind + 1] in self[word][0]:
                        # print("in first inset dict")
                        self[word][0][words_list[ind + 1]][0] += 1
                        if words_list[ind + 2] in self[word][0][words_list[ind+1]][1]:
                            # print("in second inset dict")
                            self[word][0][words_list[ind+1]][1][words_list[ind+2]] += 1
                        else:
                            # print("in first not second")
                            self[word][0][words_list[ind+1]][1][words_list[ind+2]] = 1
                        self[word][0][words_list[ind+1]][2] += 1
                    else:
                        # print("not in first inset dict")
                        self[word][0][words_list[ind + 1]] = [1, {words_list[ind+2]: 1}, 1]
                    self[word][1] += 1
                except:
                    pass
            else:
                try: 
                    # print("new entry")
                    self[word] = [{words_list[ind+1]: [1, {words_list[ind+2]: 1}, 1]}, 1]
                    # self[word][1][words_list[ind + 1]] = 1
                    # self[word].append(1)
                except:
                    pass

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]
        else:
            return 0
    
    def count_to_possibility(self):
        for value in self.values():
            prev_val = 0
            for value_next in value[0].values():
                value_next[0] = value_next[0]/value[1]+prev_val
                prev_val = value_next[0]
                prev_nexts_val = 0
                for value_next_next in value_next[1].values():
                    # print(value, ": ", key_next_next, value_next_next)
                    value_next_next = value_next_next/value_next[2]+prev_nexts_val
                    prev_nexts_val = value_next_next

    # {START: [{word1: [count, {word2: count}, total]}, total]}
    def sample(self):
        prev_word = self.random_sent[len(self.random_sent)-1]
        chance = random.random()
        prev_val = 0
        choice = ""
        # try:
        if len(self.random_sent) >= 2:
            prev_prev_word = self.random_sent[len(self.random_sent)-2]
            for key, value in self[prev_prev_word][0][prev_word][1].items():
                if chance < value and chance > prev_val:
                    choice = key
                    break
                prev_val = self[prev_word][1][key]
            # print(choice)
            return choice
        else:
            for key, value in self[prev_word][0].items():
                if chance < value[0] and chance > prev_val:
                    choice = key
                    break
                prev_val = self[prev_word][0][key][0]
            # print(choice)
            return choice

    def get_sentence(self):
        next = ""
        while next != "STOP":
            # print(next)
            next = self.sample()
            if next != "START":
                self.random_sent.append(next)
    
    def print_sentence(self):
        # print(" ".join(self.random_sent[1:len(self.random_sent)-1]))
        return " ".join(self.random_sent[1:len(self.random_sent)-1])


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) == 1:
        words = utility.read(arguments[0])
        # print(words)
        words = utility.cleanse(words)
        # print(words)
        histogram = Dictogram(words)
        histogram.count_to_possibility()
        # print(histogram)
        histogram.get_sentence()
        print(histogram.print_sentence())

if __name__ == '__main__':
    main()