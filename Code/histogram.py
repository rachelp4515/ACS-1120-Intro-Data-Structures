import random
from distutils.command.clean import clean
from pprint import pprint


def read_file(filename):
  f = open(filename, 'r', encoding='utf-8-sig')
  words = f.read()
  f.close()
  return words

def listogram(source_text):
    with open(source_text, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        clean_source = sorted([word.strip("""'",..:-—“?!();""") for word in split_source])
        listogram = []
        for word in clean_source:
            if len(listogram) == 0:
                listogram.append([word, 1])
            else:
                if word == listogram[-1][0]:
                    listogram[-1][1] +=1
                else:
                    listogram.append([word, 1])
        return listogram

def unique_words_list(hist):
   return len(listogram(hist))

def list_frequency(word, histogram):
  for histogram_word in histogram:
    if word == histogram_word[0]:
      return histogram_word[1]
  return 'Word not in text'



# pprint(listogram('alice.txt'))
# pprint(unique_words_list('fish.txt'))
# pprint(list_frequency('fish', 'fish.txt'))



#-----------------------------------------dictionary 

def dictogram(source_text):
    with open(source_text, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        hist = {}
        for word in split_source:
            clean_word = word.strip("""'",..:-—“?!();""")
            if clean_word in hist:

                hist[clean_word] += 1
            else:
                hist[clean_word] = 1
        return hist

def unique_words(histogram):
   return len(histogram.keys())

def frequency(word, histogram):
    return histogram[word]

hist = dictogram("fish.txt")
# pprint(hist)
# print(f' Unique Words: {unique_words(hist)}')
# print(f' Your word appears {frequency("alice", hist)} times.')

def random_word(hist):
    return random.choice(list(hist.keys()))

# print(random_word(hist))

