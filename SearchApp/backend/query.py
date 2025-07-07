import pickle 
from triestructure import Trie
import os

with open ('trie.pkl', 'rb') as f :
    trie = pickle.load(f)

while(True) :
    os.system('cls' if os.name == 'nt' else 'clear')
    prefix = input("Enter the string : ").strip()
    if(prefix == "exit") :
        break

    suggestions = trie.get_top_k(prefix)
    print("Top k")
    print(suggestions)
    input("Press Enter to continue")