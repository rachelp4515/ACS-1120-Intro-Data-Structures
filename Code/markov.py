from histogram import dictogram, read_file
from dictogram import Dictogram
# file = './data/fish.txt'
file = 'fish.txt'


word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace(
    '’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()


def dict_of_histograms_generator(word_list):
    start = word_list[0]
    dict_of_histograms = {}
    for i in range(len(word_list) - 1):
        word = word_list[i]
        next_word = word_list[i + 1]
        if word not in dict_of_histograms:
            histogram = Dictogram()
            histogram.add_count(next_word)
            dict_of_histograms[word] = histogram
        else:
            dict_of_histograms[word].add_count(next_word)
    return dict_of_histograms


def tweet_generator(markov_chain_dict):
    tweet = ''
    start = next(iter(markov_chain_dict))
    tweet += start
    char_limit = 140

    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        last_word = tweet_list[-1]
        last_word_histogram = markov_chain_dict[last_word]
        next_word = last_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet


if __name__ == '__main__':
    markov_chain = dict_of_histograms_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)

# from dictogram import Dictogram
# from random import choice, random


# class MarkovChain:

#     def __init__(self, word_list):


#         #The Markov chain will be a dictionary of dictionaries
#         #Example: for "one fish two fish red fish blue fish"
#         #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
#          self.markov_chain = self.build_markov(word_list)
#          self.first_word = list(self.markov_chain.keys())[0]

#     def build_markov(self, word_list):
#         markov_chain = {}

#         for i in range(len(word_list) - 1):
#             #get the current word and the word after
#             current_word = word_list[i]
#             next_word = word_list[i+1]

#             if current_word in markov_chain.keys(): #already there
#                 #get the histogram for that word in the chain
#                 histogram = markov_chain[current_word]
#                 #add to count
#                 histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
#             else: #first entry
#                 markov_chain[current_word] = Dictogram([next_word])

#         return markov_chain

#     def walk(self, length=30):
#         #TODO: generate a sentence num_words long using the markov chain
#         words = []
#         start = choice(self.starts)
#         # print('got start:', start)
#         # print('starts', self.starts, '\n')
#         # print('ends', self.ends)
        
#         current_word = self.get_next_word(start)
#         while current_word not in self.ends and len(words) < length and current_word is not None:
#             # print(current_word)
#             words.append(current_word)
#             current_word = self.get_next_word(current_word)
            
#         return words

#     def print_chain(self):
#         for word, histogram in self.markov_chain.items():
#             print(word, histogram.dictionary_histogram)





# markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
# markov_chain.print_chain()
# print(markov_chain.walk(10))