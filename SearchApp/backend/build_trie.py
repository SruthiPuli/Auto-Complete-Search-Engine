import pickle
from triestructure import Trie, TrieNode

def main() :
    trie = Trie()

    with open('words.txt', 'r') as file :

        for line in file :
            parts = line.strip().split()
            if(len(parts) > 2) :
                continue

            word, rank = parts[0], int(parts[1])

            trie.insert(rank, word)

    with open('trie.pkl', 'wb') as f :
        pickle.dump(trie, f)

main()
        

    