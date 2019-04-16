from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, string, random


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
        if words_list is not None:
            for word in words_list:
                self.add_count(word)

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
            prev_next_val = 0
            for key_next, value_next in value[1].items():
                value[1][key_next] = value_next / value[2] + prev_next_val
                prev_next_val = value[1][key_next]

    def sample(self):
        prev_word = self.random_sent[len(self.random_sent) - 1]
        chance = random.random()
        prev_val = 0
        choice = ""
        for key, value in self[prev_word][1].items():
            if chance < value and chance > prev_val:
                choice = key
                break
            prev_val = self[prev_word][1][key]
        return choice

    def get_sentence(self):
        next = ""
        while next != "STOP":
            next = self.sample()
            if next != "START":
                self.random_sent.append(next)

    def print_sentence(self):
        sentence = " ".join(self.random_sent[1 : len(self.random_sent) - 1])
        return sentence[0].capitalize() + sentence[1:] + "."


def main():
    import sys

    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) == 1:
        words = utility.read(arguments[0])
        words = utility.cleanse(words)
        histogram = Dictogram(words)
        histogram.count_to_possibility()
        histogram.get_sentence()
        print(histogram.print_sentence())


if __name__ == "__main__":
    main()
