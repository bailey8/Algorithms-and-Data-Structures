import collections

# A TRIE HAS A DICTIONARY OF CHILDREN
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # INSERT A CHARACTER INTO THE TRIE
    def insert(self, word):

        # EXTRACT THE ROOT OF THE TRIE
        current = self.root
        for letter in word:
            current = current.children[letter]

        # THE LAST CHARACTER IN THE TRIE TREE WILL BE A WORD, SO MARK IT AS SUCH
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

dic = {"a":1}
b = dic.get("o")
print(b)


import collections

a = collections.defaultdict(int)
if not a[99]:
    print(a.items())