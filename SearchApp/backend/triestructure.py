import heapq as heap 
import pickle 
from typing import *

class TrieNode :
    def __init__(self) :
        self.word = ""
        self.end = False 
        self.children = [None for _ in range(29)]
        self.top_words = []
        self.length = 0

    def add_to_top(self, rank : int, word : str) -> None :
        heap.heappush(self.top_words, (-rank, word))
        self.length += 1

        if(self.length > 10) :
            heap.heappop(self.top_words) 
            self.length -= 1 

class Trie() :
    def __init__(self) :
        self.root = TrieNode()

    def insert(self, rank : int, word : str) -> None :
        node = self.root 

        for ch in word :
            ind = 0
            if(ch == ' ') : ind = 26
            elif(ch == '-') : ind = 27
            elif(ch == '\'') : ind = 28
            else : ind = ord(ch.lower()) - 97 
            if(not node.children[ind]) :
                node.children[ind] = TrieNode()

            node = node.children[ind]
            node.add_to_top(rank, word)

        node.end = True
        node.word = word

    def get_top_k(self, prefix : str) -> List[str] :

        node = self.root 
        for ch in prefix :

            ind = ord(ch.lower()) - 97 
            if not node.children[ind] :
                return []
            
            node = node.children[ind]

        return [word for rank, word in sorted(node.top_words, reverse=True)]
