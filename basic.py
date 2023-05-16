class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.definition = None

class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, definition):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.definition = definition

    def search_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_word:
            return node.definition
        else:
            return None

# Creating an instance of the dictionary
my_dictionary = Dictionary()

# Adding words and definitions to the dictionary
my_dictionary.add_word("apple", "A fruit with red or green skin and a crisp flesh")
my_dictionary.add_word("banana", "An elongated, edible fruit with a yellow skin")
my_dictionary.add_word("cat", "A small domesticated carnivorous mammal with soft fur")

# Searching for a word in the dictionary
search_word = input("Enter a word to search in the dictionary: ")
definition = my_dictionary.search_word(search_word)

if definition:
    print(f"Definition: {definition}")
else:
    print("Word not found in the dictionary.")
