from random import choice
from dictogram import Dictogram


class Markov2():
    
    def __init__(self, tokens) -> None:
        self.chain = {}
        self.ends = []
        self.starts = []
        self.hist = Dictogram()
        
        for i in range(len(tokens)-2):
            pair = (tokens[i], tokens[i+1])
            next_pair = (tokens[i+1], tokens[i+2])
            self.hist.add_count(pair)
            
            if pair in self.chain.keys():
                self.chain[pair].append(tokens[i+2])
            else:
                self.chain[pair] = [tokens[i+2]]
                
            if '.' in tokens[i+1]:
                self.starts.append(pair)
                self.ends.append(next_pair)
        
    
    def walk(self, length=10) -> str:
        words = []
        pairs = []
        start = self.hist.sample()
        
        current_pair = start
        while len(pairs) <= length and current_pair:
            pairs.append(current_pair)
            new_word = self.get_next_word(current_pair)
            new_pair = (current_pair[len(current_pair)-1], new_word)
            # print(current_pair, new_word, new_pair)
            current_pair = new_pair
            
        # pprint(pairs)
        
        for pair in pairs:
            if pair is not pairs[len(pairs)-1]:
                words.append(pair[1])
        
        # print(words)
        
        sentence = ''
        for word in words:
            sentence += word + ' '
        
        return sentence
    
    def get_next_word(self, pair):
        if pair not in self.chain.keys():
            return None
        choices = self.chain.get(pair)
        return choice(choices)